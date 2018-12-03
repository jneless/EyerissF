import numpy as np
import conf
import IO2
import Pooling
import Activiation

class Hive():

    def __init__(self, EyerissF, mode="auto"):
        self.mode = mode
        self.EyerissF = EyerissF

    def input(self, Pictures, FilterWeights, PictureNum, FilterWeightNum):

        # check the state, input data must be compressed before
        assert np.ndim(Pictures[0]) == 1
        assert np.ndim(FilterWeights[0]) == 1

        Pictures = self.Decompress(Pictures)
        FilterWeights = self.Decompress(FilterWeights)

        self.Pictures = Pictures
        self.FilterWeights = FilterWeights
        self.PictureNum = PictureNum
        self.FilterWeightNum = FilterWeightNum

    def Conv2LogicalMapping(self):
        Pictures = self.Pictures
        FilterWeights = self.FilterWeights

        if self.PictureNum == 1:
            self.__FmapReuse__(Pictures, FilterWeights)
        elif self.FilterWeightNum == 1:
            self.__FilterReuse__(Pictures, FilterWeights)
        else:
            self.__ChannelAccumulation__(Pictures, FilterWeights)

    def Conv2PhysicalMapping(self):

        FilterWeight = self.FilterWeight
        Picture = self.Picture
        FilterWeight = self.FilterWeight
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

    def Relu(self, array):
        if type(array) == type(list()):
            return Activiation.ReluArray(array)
        else:
            return Activiation.Relu(array)

    def Pooling(self, array, activation=1):
        if type(array) == type(list()):
            return Pooling.Pooling(array, activation)
        else:
            return Pooling.MAXPooling(array, activation)

    def Compress(self, NpArray, RateNeed=0):
        if type(NpArray) == type(list()):
            return IO2.CompressArray(NpArray)
        else:
            return IO2.Compress(NpArray, RateNeed)

    def Decompress(self, NpArray):
        if type(NpArray) == type(list()):
            return IO2.DecompressArray(NpArray)
        else:
            return IO2.Decompress(NpArray)

    def Conv2d(self, Pictures=0, FilterWeights=0, PictureNum=0, FilterWeightNum=0):
        if self.mode == "auto":

            # auto mode should compress data inside
            Pictures = self.Compress(Pictures)
            FilterWeights = self.Compress(FilterWeights)

            self.input(Pictures, FilterWeights, PictureNum, FilterWeightNum)
            self.Conv2LogicalMapping()
            self.Conv2PhysicalMapping()
            self.mode = "manual"
            self.Conv2d(0, 0, 0, 0)
            self.mode = "auto"
            self.Reverse()
            return self.Output()

        else:
            map = self.mapping
            self.t = [self.EyerissF.Conv2d(x, self.FilterWeight, self.PictureNum, self.FilterWeightNum) for x in map]
            self.TempPsum = np.vstack(self.t)

    def __SetPicAndFlt__(self, Picture, FilterWeight):
        self.Picture = Picture
        self.FilterWeight = FilterWeight

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

        self.__SetPicAndFlt__(Pictures[0], FilterWeight)

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
        self.__SetPicAndFlt__(Picture, FilterWeights[0])

    def __SetPhysicalMapping__(self, mapping):
        self.mapping = mapping

    def Reverse(self):
        Psum = self.TempPsum
        if self.PictureNum == 1 and self.FilterWeightNum == 1:
            self.__SetReturnImgs__(Psum)
        if self.PictureNum == 1:
            self.__ReverseFmapReuse__(Psum, self.FilterWeightNum)
        elif self.FilterWeightNum == 1:
            self.__ReverseFilterReuse__(Psum, self.PictureNum)

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

        # self.__SetReturnImgs__(np.array(m))
        self.__SetReturnImgs__(m)

    def __ReverseFilterReuse__(self, Psum, PsumNum):
        self.__SetReturnImgs__(list(np.hsplit(Psum, PsumNum)))

    def __SetReturnImgs__(self, ReturnImgs):
        self.ReturnImgs = ReturnImgs

    def Output(self):
        return self.Compress(self.ReturnImgs)

    def FullConnect(self, v1, v2, activation=1):
        return np.array(np.dot(v1, v2) / activation, dtype=int)
