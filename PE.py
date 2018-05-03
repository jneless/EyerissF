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

    def __Conv1d__(self, ImageRow, FilterWeight):
        result = list()
        for x in range(0, len(ImageRow) - 1 + len(FilterWeight)):
            y = x + len(FilterWeight)
            if y > len(ImageRow):
                break
            r = ImageRow[x:y] * FilterWeight
            result.append(r.sum())
        return np.array(result)

    def __Conv1dCodingTest__(self, ImageRow, FilterWeight,ImageNum,FilterNum):


        l=list()


        if FilterNum==1 and ImageNum==1:

            # 图和核都为1 直接运行卷积
            return self.__Conv1d__(ImageRow, FilterWeight)
        else:

            # 核为1 ， Image重用
            if FilterNum==1:

                # 分割图为原始的小型图
                pics=np.vsplit(ImageRow,ImageNum)

                # 遍历，卷积
                for x in pics:

                    # 卷积后的结果加入l中临时保存
                    l.append(self.__Conv1d__(x,FilterWeight))

                    # 将l中的结果组合成一个新的矩阵
                    # 横向组合
                    result=np.vstack(np.array(l))

                # 返回结果
                return result

            # 图为1 ，filter重用
            if ImageNum==1:

                # 将ImageRow变为矩阵
                ImageRow=np.reshape(ImageRow,(ImageRow.size/ImageNum,ImageNum))
                flts=ImageRow=np.array(ImageRow.T)
                for x in flts:
                    l.append(self.__Conv1d__(ImageRow,x))
                result = np.array(l)
                result=result.T
                result=np.reshape(result,(1,result.size))
                return result



                '''
                多个filter是打乱之后传入
                需要先变成正常形状，再卷积，再把卷积结果打乱传出
                上层接受到以后，再把打乱的结果变成正常结果
                '''



                ...

        #TODO 加入多channel的情况

    def CountPsum(self):

        if self.PEState == conf.ClockGate:
            self.Psum = conf.EmptyPsum
        elif self.PEState == conf.Running:
            self.Psum = self.__Conv1d__(self.ImageRow,self.FilterWeight)

        return self.Psum

if __name__ == '__main__':

    p = PE()
    p.PEState=conf.Running
    p.SetFilterWeight(np.array([1, 1, 1]))
    p.SetImageRow(np.array([1, 1, 1, 1, 1]))
    r=p.CountPsum()
    print(r)
