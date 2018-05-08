import conf
from IOCompression import *


class Compiler:

    def __init__(self, EyerissF):
        self.EyerissF = EyerissF

    def input(self, Picture, FilterWeight, PictureNum, FilterNum):

        Picture, FilterWeight = InputDecompress(Picture, FilterWeight)

        self.Picture = Picture
        self.FilterWeight = FilterWeight
        self.PictureNum = PictureNum
        self.FilterNum = FilterNum

    def __SetPicAndFlt__(self, Picture, FilterWeight):
        self.Picture = Picture
        self.FilterWeight = FilterWeight

    def __SetPhysicalMapping__(self, mapping):
        self.mapping = mapping

    def __SetReturnImgs__(self, ReturnImgs):
        self.ReturnImgs = ReturnImgs

    def GetReturnImgs(self):
        r = OutputCompress(self.ReturnImgs)
        return r

    def Con2LogicalMapping(self):

        Pictures = self.Picture
        FilterWeights = self.FilterWeight

        if self.PictureNum == 1:
            self.__FmapReuse__(Pictures, FilterWeights)
        elif self.FilterNum == 1:
            self.__FilterReuse__(Pictures, FilterWeights)
        else:
            self.__ChannelAccumulation__(Pictures, FilterWeights)

    def Con2PhysicalMapping(self):

        FilterWeight = self.FilterWeight

        if self.PictureNum == 1:  # 一个图片多个卷积核
            Picture = self.Picture[0]
            FilterWeight = self.FilterWeight


        elif self.FilterNum == 1:  # 一个卷积核，多个图片
            Picture = self.Picture
            FilterWeight = self.FilterWeight[0]

        x = 0
        t = list()
        while conf.EyerissWidth * x + conf.EyerissWidth + len(FilterWeight) - 1 < len(FilterWeight) + len(Picture) - 1:
            P = Picture[conf.EyerissWidth * x: conf.EyerissWidth * x + conf.EyerissWidth + len(FilterWeight) - 1]
            x = x + 1
            t.append(P)

        P = Picture[conf.EyerissWidth * x:]

        # 判断逻辑矩阵的尾巴，并删除多余的图
        if len(Picture[conf.EyerissWidth * x:]) < len(FilterWeight):
            pass
        else:
            t.append(P)

        self.__SetPhysicalMapping__(t)

    def Conv2d(self):

        t = []
        map = self.mapping

        for x in map:

            if self.FilterNum == 1:
                w = self.EyerissF.Conv2d(x, self.FilterWeight[0], self.PictureNum, self.FilterNum)
            elif self.PictureNum == 1:
                w = self.EyerissF.Conv2d(x, self.FilterWeight, self.PictureNum, self.FilterNum)

            t.append(w)

        self.TempPsum = np.vstack(t)

    def Reverse(self):

        Psum = self.TempPsum

        if self.PictureNum == 1:
            # return self.__ReverseFmapReuse__(Psum, self.FilterNum)
            self.__ReverseFmapReuse__(Psum, self.FilterNum)

        elif self.FilterNum == 1:
            # return self.__ReverseFilterReuse__(Psum, self.PictureNum)
            self.__ReverseFilterReuse__(Psum, self.PictureNum)

    def __FmapReuse__(self, Pictures, FilterWeights):

        assert len(Pictures) == 1

        NewArray = list()
        NewArrayLines = list()

        for x in range(0, len(FilterWeights[0])):
            # third, move the next pic NewArray
            for y in range(0, len(FilterWeights[0][0])):
                # second, in the same NewArray do the same operations
                for z in range(0, len(FilterWeights)):
                    # first, write different pics' pixs in a NewArray
                    NewArrayLines.append(FilterWeights[z][x][y])
            NewArray.append(np.hstack(NewArrayLines))
            NewArrayLines.clear()
        FilterWeight = np.array(NewArray)

        self.__SetPicAndFlt__(Pictures, FilterWeight)

    def __FilterReuse__(self, Pictures, FilterWeights):

        assert len(FilterWeights) == 1

        l = list()
        line = list()
        for y in range(0, len(Pictures[0])):
            # second move to next line to loop the inner operations
            for x in range(0, len(Pictures)):
                # first combine two lines ,which locate on different pics, to one line
                l.append(Pictures[x][y])
            line.append(np.hstack(l))
            l.clear()
        Picture = np.array(line)
        self.__SetPicAndFlt__(Picture, FilterWeights)

    def __ChannelAccumulation__(self, Pictures, FilterWeights):

        line = list()
        l = list()

        for x in range(0, len(Pictures[0])):
            for y in range(0, len(Pictures[0][0])):
                for z in range(0, len(Pictures)):
                    l.append(Pictures[z][x][y])
            line.append(np.hstack(l))
            l.clear()
        Picture = np.array(line)
        line.clear()

        for x in range(0, len(FilterWeights[0])):
            for y in range(0, len(FilterWeights[0][0])):
                for z in range(0, len(FilterWeights)):
                    l.append(FilterWeights[z][x][y])
            line.append(np.hstack(l))
            l.clear()
        FilterWeight = np.array(line)
        line.clear()

        self.__SetPicAndFlt__(Picture, FilterWeight)

    def __ReverseFmapReuse__(self, Psum, PsumNum):

        SubMap = np.hsplit(Psum, int(np.shape(Psum)[1] / PsumNum))

        l = []
        m = []

        for x in range(0, PsumNum):
            for y in range(len(SubMap)):
                # [np.newaxis]会使返回的向量为列向量
                l.append(np.transpose(np.array(SubMap[y][:, x])[np.newaxis]))
            m.append(np.hstack(l))
            l = []

        # return m
        self.__SetReturnImgs__(np.array(m))

    def __ReverseFilterReuse__(self, Psum, PsumNum):

        # return np.hsplit(Psum, PsumNum)
        self.__SetReturnImgs__(np.hsplit(Psum, PsumNum))


if __name__ == "__main__":
    ...
