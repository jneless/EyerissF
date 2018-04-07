import numpy as np
import conf
import Activiation
from PE import PE

class EyerissF:

    GlobalBuffer=conf.SRAMSize
    EyerissWidth=conf.EyerissWidth
    EyerissHeight=conf.EyerissHeight

    def __init__(self):
        pass

    def Conv2d(self,Pictures,FilterWights,Activation='Relu'):
        self.RawStationry(Pictures,FilterWights)
        self.DataDeliver()
        self.run()
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

    def DataDeliver(self):
        #将一个pic和filter分发到eyeirss中
        pass

    def FmapReuse(self,Pictures,FilterWights):
        line = list()
        l = list()
        Picture = Pictures
        for x in range(0, len(FilterWights[0])):
            # third, move the next pic line
            for y in range(0, len(FilterWights[0][0])):
                # second, in the same line do the same operations
                for z in range(0, len(FilterWights)):
                    # first, write different pics' pixs in a line
                    l.append(FilterWights[z][x][y])
            line.append(np.hstack(l))
            l.clear()
        FilterWight = np.array(line)
        return Picture, FilterWight

    def FilterReuse(self,Pictures,FilterWights):
        FilterWight=FilterWights
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
        return Picture, FilterWight

    def ChannelAccumulation(self,Pictures,FilterWights):
        pass

    def run(self):
        pass

    def RawStationry(self,Pictures,FilterWights):
        # Call Two Reuse function and ChannelAccumulation
        pass