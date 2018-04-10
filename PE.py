import numpy as np
import conf

class PE:

    PEBuffer=conf.PEBuffer
    PEState=conf.ClockGate

    def __init__(self):
        self.setFilterWeight((0,0))
        self.setImageRow((0,0))

    def SetPEState(self,State):
        self.PEState=State

    def SetFilterWeight(self,FilterWeight):
        self.FilterWeight=FilterWeight

    def SetImageRow(self, ImageRow):
        self.ImageRow = ImageRow

    def Conv1d(self,ImageRow,FilterWeight):
        result = list()
        for x in range(0,len(ImageRow)-1+len(FilterWeight)):
            y=x+len(FilterWeight)
            if y>len(ImageRow):
                break
            r=ImageRow[x:y]*FilterWeight
            result.append(r.sum())
        return np.array(result)

    def CountPsum(self):

        #############
        #
        # ### First Edition ###
        #
        # try:
        #     self.Psum=self.Conv1d(self.FilterWeight,self.ImageRow)
        # except:
        #     pass
        #
        #############

        if self.PEState==conf.ClockGate:
            self.Psum=conf.EmptyPsum
        elif self.PEState==conf.Running:
            self.Psum = self.Conv1d(self.FilterWeight, self.ImageRow)


if __name__=='__main__':
    p=PE()
    r=p.Conv1d(np.array([1,1,1,1,1]),np.array([1,1]))
    print(r)
