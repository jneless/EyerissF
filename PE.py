import numpy as np
import conf


class PE:
    PEBuffer = conf.PEBuffer
    PEState = conf.ClockGate

    def __init__(self):
        self.SetFilterWeight((0, 0))
        self.SetImageRow((0, 0))

    def SetPEState(self, State):
        self.PEState = State

    def SetFilterWeight(self, FilterWeight):
        self.FilterWeight = FilterWeight

    def SetImageRow(self, ImageRow):
        self.ImageRow = ImageRow

    def Conv1d(self, ImageRow, FilterWeight):
        result = list()
        for x in range(0, len(ImageRow) - 1 + len(FilterWeight)):
            y = x + len(FilterWeight)
            if y > len(ImageRow):
                break

            # Eyeriss有跳0操作，但此处代码没体现
            r = ImageRow[x:y] * FilterWeight
            result.append(r.sum())
        return np.array(result)

    def CountPsum(self):

        if self.PEState == conf.ClockGate:
            self.Psum = conf.EmptyPsum
        elif self.PEState == conf.Running:
            self.Psum = self.Conv1d(self.ImageRow,self.FilterWeight)

        return self.Psum


if __name__ == '__main__':
    p = PE()
    p.PEState=conf.Running
    p.SetFilterWeight(np.array([1, 1, 1]))
    p.SetImageRow(np.array([1, 1, 1, 1, 1]))
    r=p.CountPsum()
    print(r)
