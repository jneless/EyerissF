from Hive import Hive
from EyerissF import EyerissF as EF
import numpy as np
import Extension
import skimage.io as io

# ef = EF()
# hive = Hive(ef)
#
# pics = [255-io.imread("Pic/01.png", as_grey=True)]
# flts = [np.load("ConvLayerFilter/ConvLayer1Filter"+str(x)+".npy") for x in range(1,7)]
#
# pics=hive.Conv2d(pics,flts,1,6)
#
# pics=hive.Pooling(hive.Decompress(pics),255)
#
# r = [hive.Conv2d(pics, [np.load("ConvLayerFilter/ConvLayer2Filter" + str(x) + ".npy")],6, 1) for x in range(1, 17)]
# pics = [Extension.NumpyAddExtension(hive.Decompress(r[x])) for x in range(16)]
#
# pics=hive.Pooling(pics,255)
#
# vector = hive.FullConnect(np.array(pics).flatten(),np.load('FullConnectLayer/FullConnectLayer1.npy'),255)
#
# vector = hive.FullConnect(vector, np.load('FullConnectLayer/FullConnectLayer2.npy'))
#
# vector = hive.FullConnect(vector, np.load('FullConnectLayer/FullConnectLayer3.npy'))
#
# print("this number is : ",vector.argmax())




# ef = EF()
# hive = Hive(ef)
#
# pics = [255-io.imread("Pic/01.png", as_grey=True)]
# flts = [np.load("ConvLayerFilter/ConvLayer1Filter"+str(x)+".npy") for x in range(1,7)]
#
# pics=hive.Conv2d(pics,flts,1,6)
#
# pics=hive.Pooling(hive.Decompress(pics),255)
#
# r = [hive.Conv2d(pics, [np.load("ConvLayerFilter/ConvLayer2Filter" + str(x) + ".npy")],6, 1) for x in range(1, 17)]
# pics = [Extension.NumpyAddExtension(hive.Decompress(r[x])) for x in range(16)]
#
# pics=hive.Pooling(pics,255)
#
# vector = hive.FullConnect(np.array(pics).flatten(),np.load('FullConnectLayer/FullConnectLayer1.npy'),255)
#
# vector = hive.FullConnect(vector, np.load('FullConnectLayer/FullConnectLayer2.npy'))
#
# vector = hive.FullConnect(vector, np.load('FullConnectLayer/FullConnectLayer3.npy'))
#
# print("this number is : ",vector.argmax())
