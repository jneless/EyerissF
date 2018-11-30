import numpy as np
import conf
from PE import PE
from Activiation import Relu

class EyerissF:
    GlobalBuffer = conf.SRAMSize
    EyerissWidth = conf.EyerissWidth
    EyerissHeight = conf.EyerissHeight

    def __init__(self):
        self.__InitPEs__()

    def Conv2d(self, Picture, FilterWeight, ImageNum, FilterNum):

        PictureColumnLength, FilterWeightColumnLength = self.__DataDeliver__(Picture, FilterWeight, ImageNum, FilterNum)
        self.__run__()
        ConvedArray = self.__PsumTransport__(PictureColumnLength, FilterWeightColumnLength)
        ReluedConvedArray = Relu(ConvedArray)
        self.__SetALLPEsState__(conf.ClockGate)

        return ReluedConvedArray

    def __InitPEs__(self, PEsWidth=conf.EyerissWidth, PEsHeight=conf.EyerissHeight):
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

        # 卷积核行数必须小于图片行数
        assert FilterWeightColumnLength <= PictureColumnLength

        # 卷积核行数必须小于Eyeriss高度
        assert FilterWeightColumnLength <= EyerissF.EyerissHeight

        # 图片行数必须小于 Eyeriss长宽只和-1
        assert PictureColumnLength <= EyerissF.EyerissHeight + EyerissF.EyerissWidth - 1

        for ColumnELement in range(0, FilterWeightColumnLength):
            for RowElement in range(0, PictureColumnLength + 1 - FilterWeightColumnLength):
                try:
                    self.PEArray[ColumnELement][RowElement].SetPEState(conf.Running)
                except:
                    pass

    def __SetALLPEImgNumAndFltNum__(self, ImageNum, FilterNum):
        for ColumnELement in range(0, EyerissF.EyerissHeight):
            for RowElement in range(0, EyerissF.EyerissWidth):
                self.PEArray[ColumnELement][RowElement].SetPEImgAndFlt(ImageNum, FilterNum)

    def __DataDeliver__(self, Picture, FilterWeight, ImageNum, FilterNum):
        # put the pic and filter row data into PEArray

        # Eyeriss越界检查
        # 卷积核行数不能超过 Eyeriss的高度（12）
        assert len(FilterWeight) <= self.EyerissHeight

        # 图片的行数不能超过 卷积核行数 + Eyeriss宽度（14） -1
        assert len(Picture) <= len(FilterWeight) + self.EyerissWidth - 1

        PictureColumnLength = len(Picture)
        FilterWeightColumnLength = len(FilterWeight)

        self.__SetALLPEImgNumAndFltNum__(ImageNum, FilterNum)
        self.__SetPEsRunningState__(PictureColumnLength, FilterWeightColumnLength)

        # filterWeight 从左到右
        for ColumnELement in range(0, len(FilterWeight)):
            for RowElement in range(0, self.EyerissWidth):
                self.PEArray[ColumnELement][RowElement].SetFilterWeight(FilterWeight[ColumnELement])

        # ImageRow 从左下到右上
        for ColumnELement in range(0, len(Picture)):
            DeliverinitR = 0
            DeliverinitH = ColumnELement
            for c in range(0, ColumnELement + 1):
                try:
                    # 当len（pic）大于12的时候会发生一场，找不到PEArray[13][0]，但是与后续不影响
                    self.PEArray[DeliverinitH][DeliverinitR].SetImageRow(Picture[ColumnELement])
                except:
                    pass

                DeliverinitR = DeliverinitR + 1
                DeliverinitH = DeliverinitH - 1

        return PictureColumnLength, FilterWeightColumnLength

    def __run__(self):
        # 整个系统开始计算

        for x in range(0, conf.EyerissHeight):
            for y in range(0, conf.EyerissWidth):
                if self.PEArray[x][y].PEState == conf.Running:
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
            result.append(np.sum(line, axis=0, dtype=int))

        # 将r中全部的卷积值组合成一个矩阵，并返回
        if result == []:
            return

        return np.vstack(result)

    def __ShowPEState__(self, x, y):
        print("PE is : ", x, ",", y)

        if self.PEArray[x][y].PEState == conf.Running:
            print("PEState : Running")

        else:
            print("PEState : ClockGate")

        print("FilterWeight :", self.PEArray[x][y].FilterWeight)
        print("ImageRow :", self.PEArray[x][y].ImageRow)

    def __ShowAllPEState__(self):

        xx = list()
        yy = list()
        for x in range(conf.EyerissHeight):
            for y in range(conf.EyerissWidth):
                self.__ShowPEState__(x, y)
                if self.PEArray[x][y].PEState == conf.Running:
                    yy.append(1)
                else:
                    yy.append(0)

            xx.append(yy)
            yy = []
        print(np.array(xx))

    def __ShowRunningPEState__(self):

        c = 0
        xx = list()
        yy = list()
        for x in range(conf.EyerissHeight):
            for y in range(conf.EyerissWidth):

                if self.PEArray[x][y].PEState == conf.Running:
                    self.__ShowPEState__(x, y)
                    c = c + 1
                    yy.append(1)
                else:
                    yy.append(0)
            xx.append(yy)
            yy = []
        print("一共有", c, "个PE正在运行")
        print(np.array(xx))

    def __ShowStates__(self):
        c = 0
        xx = list()
        yy = list()
        for x in range(conf.EyerissHeight):
            for y in range(conf.EyerissWidth):

                if self.PEArray[x][y].PEState == conf.Running:
                    c = c + 1
                    yy.append(1)
                else:
                    yy.append(0)
            xx.append(yy)
            yy = []
        print("一共有", c, "个PE正在运行")
        print(np.array(xx))
