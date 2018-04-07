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
        eval('return Activiation.' + Activation + '()')


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
        pass

    def FilterReuse(self,Pictures,FilterWights):
        pass

    def ChannelAccumulation(self,Pictures,FilterWights):
        pass


    def run(self):
        pass
