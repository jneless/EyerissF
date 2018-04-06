import numpy as np
import conf
from PE import PE

class EyerissF:

    def __init__(self):
        pass

    def Conv2d(self,Pictures,FilterWights):
        self.DataDeliver()
        pass

    def InitPEs(self,PEsWidth=conf.EyerissWidth,PEsHeight=conf.EyerissHeight):

        self.PEArray=list()
        for x in range(0,conf.EyerissHeight):
            self.PEArray.append(list())
            for y in range(0,conf.EyerissWidth):
                self.PEArray[x].append(PE())

        pass

    def DataDeliver(self):
        pass