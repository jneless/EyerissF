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

    def __Conv__(self):

        ImageRow=self.ImageRow
        FilterWeight=self.FilterWeight

        ImageNum=self.ImageNum
        FilterNum=self.FilterNum

        l=list()


        if FilterNum==1 and ImageNum==1:

            # 图和核都为1 直接运行卷积
            return self.__Conv1d__(ImageRow, FilterWeight)
        else:

            # 核为1 ， filter重用
            if FilterNum==1:

                # 分割图为原始的小型图
                pics=np.hsplit(ImageRow,ImageNum)

                # 遍历，卷积
                for x in pics:

                    # 卷积后的结果加入l中临时保存
                    l.append(self.__Conv1d__(x,FilterWeight))

                    # 将l中的结果组合成一个新的矩阵
                    # 横向组合
                    result=np.hstack(np.array(l))

                # 返回结果
                return result

            # 图为1 ，img重用
            if ImageNum==1:


                # 将FilterWeight变为矩阵
                FilterWeight = np.reshape(FilterWeight, (int(FilterWeight.size / FilterNum),FilterNum))
                flts=np.array(FilterWeight.T)

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
                
                
                示例输入[1,1,1,1],[1,2,1,2],1,2
                返回 [2 4 2 4 2 4] 是 [2,2,2] [4,4,4]的合并
                
                '''


        #TODO 加入多channel的情况

    def CountPsum(self):

        if self.PEState == conf.ClockGate:
            self.Psum = conf.EmptyPsum
        elif self.PEState == conf.Running:
            # self.Psum = self.__Conv1d__(self.ImageRow,self.FilterWeight)

            self.Psum = self.__Conv__()

        return self.Psum

    def SetPEConf(self,ImageNum,FilterNum):
        self.ImageNum=ImageNum
        self.FilterNum=FilterNum

if __name__ == '__main__':

    p = PE()
    p.SetPEState(conf.Running)

    img=np.array([1,1,1,1])
    flt = np.array([1, 2,1,2])

    p.SetPEConf(1,2)
    print(p.__Conv__(img,flt))

