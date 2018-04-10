import numpy as np
import conf
from PE import PE

class EyerissF:

    GlobalBuffer=conf.SRAMSize
    EyerissWidth=conf.EyerissWidth
    EyerissHeight=conf.EyerissHeight

    def __init__(self):
        pass

    def Conv2d(self,Pictures,FilterWeights,Activation='Relu'):
        self.RawStationry(Pictures,FilterWeights)
        self.DataDeliver()
        self.run()

        #TODO self.PsumTransport()

        self.SetALLPEsState(conf.ClockGate)
        eval('Activiation.' + Activation + '()')

        ###########################################
        # if Activiation=='Relu' :
        #     return Activiation.Relu()
        # else:
        #     eval('return Activiation.' + Activation + '()')
        ###########################################

    def InitPEs(self,PEsWidth=conf.EyerissWidth,PEsHeight=conf.EyerissHeight):
        self.PEArray=list()
        for x in range(0,conf.EyerissHeight):
            self.PEArray.append(list())
            for y in range(0,conf.EyerissWidth):
                self.PEArray[x].append(PE())

    def SetALLPEsState(self,State):

        assert State==conf.ClockGate or State==conf.Running

        for ColumnELement in range(0, EyerissF.EyerissHeight):
            for RowElement in range(0, EyerissF.EyerissWidth):
                self.PEArray[ColumnELement][RowElement].SetPEState(State)

    def SetPEsRunningState(self,PictureColumnLength,FilterWeightColumnLength):

        assert FilterWeightColumnLength <= PictureColumnLength
        assert FilterWeightColumnLength <= EyerissF.EyerissHeight
        assert PictureColumnLength <= EyerissF.EyerissHeight + EyerissF.EyerissWidth -1

        for ColumnELement in range(0, FilterWeightColumnLength):
            for RowElement in range(0, PictureColumnLength + 1 - FilterWeightColumnLength):
                self.PEArray[ColumnELement][RowElement].SetPEState(conf.Running)

    def DataDeliver(self,Picture,FilterWeight):
        # put the pic and filter row data into PEArray

        # Eyeriss scale-overflow check
        assert len(FilterWeight)<=self.EyerissHeight
        assert len(Picture)+len(Picture[0])-1 <= self.EyerissWidth

        # filterWeight input from left to right
        for ColumnELement in range(0,len(FilterWeight)):
            for RowElement in range(0,self.EyerissWidth):
                self.PEArray[ColumnELement][RowElement].SetFilterWeight(FilterWeight[x])

        # ImageRow input from left-down to righ-up

        for z in range(0,len(Picture)):
            x = 0
            y = z
            for c in range(0,z+1):
                self.PEArray[y][x].SetImageRow(Picture[z])
                x=x+1
                y=y-1

    def FmapReuse(self,Pictures,FilterWeights):

        assert len(Pictures)==1

        #TODO Rename l and line

        line = list()
        l = list()
        Picture = Pictures
        for x in range(0, len(FilterWeights[0])):
            # third, move the next pic line
            for y in range(0, len(FilterWeights[0][0])):
                # second, in the same line do the same operations
                for z in range(0, len(FilterWeights)):
                    # first, write different pics' pixs in a line
                    l.append(FilterWeights[z][x][y])
            line.append(np.hstack(l))
            l.clear()
        FilterWeight = np.array(line)
        return Picture, FilterWeight

    def FilterReuse(self,Pictures,FilterWeights):

        assert len(FilterWeights)==1

        # TODO Rename l and line

        FilterWeight=FilterWeights
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
        return Picture, FilterWeight

    def ChannelAccumulation(self,Pictures,FilterWeights):
        pass

    def run(self):
        for x in range(0,conf.EyerissHeight):
            for y in range(0,conf.EyerissWidth):
                self.PEArray[x][y].countPsum()
        #TODO

    def PsumTransport(self):
        pass

    def RawStationry(self,Pictures,FilterWeights):
        # Call Two Reuse function and ChannelAccumulation
        pass


if __name__=='__main__':
    Pic1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    Pic2 = np.array([[9, 10], [11, 12], [13, 14], [15, 16]])

    e=EyerissF()
    e.InitPEs()


    e.DataDeliver(Pic1,Pic2)
    print(e.PEArray[0][0].ImageRow)
    print(e.PEArray[1][0].ImageRow)
    print(e.PEArray[0][1].ImageRow)

    print(e.PEArray[2][0].ImageRow)
    print(e.PEArray[1][1].ImageRow)
    print(e.PEArray[0][2].ImageRow)
    e.run()



    print(e.PEArray[0][0].Psum)
    print(e.PEArray[1][0].Psum)
    print(e.PEArray[0][1].Psum)

    print(e.PEArray[2][0].Psum)
    print(e.PEArray[1][1].Psum)
    print(e.PEArray[0][2].Psum)