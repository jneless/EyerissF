import numpy as np
from EyerissF import EyerissF as EF
from Compiler import Compiler as CP


ConvLayer1Filter1=np.load('ConvLayerFilter/ConvLayer1Filter1.npy')
ConvLayer1Filter2=np.load('ConvLayerFilter/ConvLayer1Filter2.npy')
ConvLayer1Filter3=np.load('ConvLayerFilter/ConvLayer1Filter3.npy')
ConvLayer1Filter4=np.load('ConvLayerFilter/ConvLayer1Filter4.npy')
ConvLayer1Filter5=np.load('ConvLayerFilter/ConvLayer1Filter5.npy')
ConvLayer1Filter6=np.load('ConvLayerFilter/ConvLayer1Filter6.npy')
pic=np.load('Pic/pic.npy')

cp=CP()
ef=EF()

Picture, FilterWeight,PictureNum,FilterWeightNum=cp.Con2LogicalMapping(pic[np.newaxis],FilterWeights=(ConvLayer1Filter1,ConvLayer1Filter2,
	ConvLayer1Filter3,ConvLayer1Filter4,ConvLayer1Filter5,ConvLayer1Filter6))

t=list()
for x in cp.Con2PhysicalMapping(Picture[0], FilterWeight,PictureNum,FilterWeightNum):
    w=ef.Conv2d(x,FilterWeight)
    t.append(w)

bb=np.vstack(t)
print(bb.shape)


