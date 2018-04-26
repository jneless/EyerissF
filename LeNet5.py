import numpy as np
from EyerissF import EyerissF as EF
from Compiler import Compiler as CP


ConvLayer1Filter1=np.load('ConvLayerFilter/ConvLayer1Filter1.npy')
ConvLayer1Filter2=np.load('ConvLayerFilter/ConvLayer1Filter2.npy')
ConvLayer1Filter3=np.load('ConvLayerFilter/ConvLayer1Filter3.npy')
ConvLayer1Filter4=np.load('ConvLayerFilter/ConvLayer1Filter4.npy')
ConvLayer1Filter5=np.load('ConvLayerFilter/ConvLayer1Filter5.npy')
ConvLayer1Filter6=np.load('ConvLayerFilter/ConvLayer1Filter6.npy')

ConvLayer2Filter1=np.load('ConvLayerFilter/ConvLayer2Filter1.npy')
ConvLayer2Filter2=np.load('ConvLayerFilter/ConvLayer2Filter2.npy')
ConvLayer2Filter3=np.load('ConvLayerFilter/ConvLayer2Filter3.npy')
ConvLayer2Filter4=np.load('ConvLayerFilter/ConvLayer2Filter4.npy')
ConvLayer2Filter5=np.load('ConvLayerFilter/ConvLayer2Filter5.npy')
ConvLayer2Filter6=np.load('ConvLayerFilter/ConvLayer2Filter6.npy')
ConvLayer2Filter7=np.load('ConvLayerFilter/ConvLayer2Filter7.npy')
ConvLayer2Filter8=np.load('ConvLayerFilter/ConvLayer2Filter8.npy')
ConvLayer2Filter9=np.load('ConvLayerFilter/ConvLayer2Filter9.npy')
ConvLayer2Filter10=np.load('ConvLayerFilter/ConvLayer2Filter10.npy')

ConvLayer2Filter11=np.load('ConvLayerFilter/ConvLayer2Filter11.npy')
ConvLayer2Filter12=np.load('ConvLayerFilter/ConvLayer2Filter12.npy')
ConvLayer2Filter13=np.load('ConvLayerFilter/ConvLayer2Filter13.npy')
ConvLayer2Filter14=np.load('ConvLayerFilter/ConvLayer2Filter14.npy')
ConvLayer2Filter15=np.load('ConvLayerFilter/ConvLayer2Filter15.npy')
ConvLayer2Filter16=np.load('ConvLayerFilter/ConvLayer2Filter16.npy')

pic=np.load('Pic/pic.npy')

cp=CP()

ef=EF()
ef.InitPEs()


Picture, FilterWeight=cp.RawStationry(pic[np.newaxis],FilterWeights=(ConvLayer1Filter1,ConvLayer1Filter2,
	ConvLayer1Filter3,ConvLayer1Filter4,ConvLayer1Filter5,ConvLayer1Filter6))


