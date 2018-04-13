import numpy as np
import conf
from PE import PE
from Activiation import Relu


class EyerissF:
    GlobalBuffer = conf.SRAMSize
    EyerissWidth = conf.EyerissWidth
    EyerissHeight = conf.EyerissHeight

    def __init__(self):
        pass

    def Conv2d(self, Picture, FilterWeight):
        PictureColumnLength, FilterWeightColumnLength = self.__DataDeliver__(Picture, FilterWeight)
        self.__run__()
        ConvedArray = self.__PsumTransport__(PictureColumnLength, FilterWeightColumnLength)
        ReluedConvedArray = Relu(ConvedArray)
        self.__SetALLPEsState__(conf.ClockGate)
        return ReluedConvedArray

    def InitPEs(self, PEsWidth=conf.EyerissWidth, PEsHeight=conf.EyerissHeight):
        self.PEArray = list()
        for x in range(0, PEsHeight):
            self.PEArray.append(list())
            for y in range(0, PEsWidth):
                self.PEArray[x].append(PE())

    def __SetALLPEsState__(self, State):

        assert State == conf.ClockGate or State == conf.Running

        for ColumnELement in range(0, EyerissF.EyerissHeight):
            for RowElement in range(0, EyerissF.EyerissWidth):
                self.PEArray[ColumnELement][RowElement].SetPEState(State)

    def __SetPEsRunningState__(self, PictureColumnLength, FilterWeightColumnLength):

        assert FilterWeightColumnLength <= PictureColumnLength
        assert FilterWeightColumnLength <= EyerissF.EyerissHeight
        assert PictureColumnLength <= EyerissF.EyerissHeight + EyerissF.EyerissWidth - 1

        for ColumnELement in range(0, FilterWeightColumnLength):
            for RowElement in range(0, PictureColumnLength + 1 - FilterWeightColumnLength):
                self.PEArray[ColumnELement][RowElement].SetPEState(conf.Running)

    def __DataDeliver__(self, Picture, FilterWeight):
        # put the pic and filter row data into PEArray

        # Eyeriss scale-overflow check
        assert len(FilterWeight) <= self.EyerissHeight
        assert len(Picture) + len(Picture[0]) - 1 <= self.EyerissWidth

        PictureColumnLength = len(Picture)
        FilterWeightColumnLength = len(FilterWeight)

        self.__SetPEsRunningState__(PictureColumnLength, FilterWeightColumnLength)

        # filterWeight input from left to right
        for ColumnELement in range(0, len(FilterWeight)):
            for RowElement in range(0, self.EyerissWidth):
                self.PEArray[ColumnELement][RowElement].SetFilterWeight(FilterWeight[ColumnELement])

        # ImageRow input from left-down to righ-up
        for z in range(0, len(Picture)):
            x = 0
            y = z
            for c in range(0, z + 1):
                self.PEArray[y][x].SetImageRow(Picture[z])
                x = x + 1
                y = y - 1

        return PictureColumnLength, FilterWeightColumnLength

    def __run__(self):
        for x in range(0, conf.EyerissHeight):
            for y in range(0, conf.EyerissWidth):
                self.PEArray[x][y].CountPsum()

    def __PsumTransport__(self, PictureColumnLength, FilterWeightColumnLength):

        line = list()
        result = list()
        for RowElement in range(0, PictureColumnLength + 1 - FilterWeightColumnLength):

            # 清空list
            line.clear()
            for ColumnElement in range(0, FilterWeightColumnLength).__reversed__():
                # 从上到下把psum加入list
                line.append(self.PEArray[ColumnElement][RowElement].Psum)

            # 将list中的Psum做和，得到一行卷积值，保存到r中
            result.append(np.sum(line, axis=0))

        # 将r中全部的卷积值组合成一个矩阵，并返回
        return np.vstack(result)



if __name__ == '__main__':

    Pic1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    Pic2 = np.array([[9, 10], [11, 12], [13, 14], [15, 16]])

    e = EyerissF()
    e.InitPEs()

    e.__DataDeliver__(Pic1, Pic2)
    print(e.PEArray[0][0].ImageRow)
    print(e.PEArray[1][0].ImageRow)
    print(e.PEArray[0][1].ImageRow)

    print(e.PEArray[2][0].ImageRow)
    print(e.PEArray[1][1].ImageRow)
    print(e.PEArray[0][2].ImageRow)
    e.__run__()

    print(e.PEArray[0][0].Psum)
    print(e.PEArray[1][0].Psum)
    print(e.PEArray[0][1].Psum)

    print(e.PEArray[2][0].Psum)
    print(e.PEArray[1][1].Psum)
    print(e.PEArray[0][2].Psum)
