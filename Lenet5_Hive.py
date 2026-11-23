from Hive import Hive
from EyerissF import EyerissF as EF
import numpy as np
import Extension
from PIL import Image

ef = EF()
hive = Hive(ef)

pics = [255-np.asarray(Image.open("Pic/01.png").convert("L"))]
flts = [np.load("ConvLayerFilter/ConvLayer1Filter"+str(x)+".npy") for x in range(1,7)]

pics=hive.Conv2d(pics,flts,1,6)

pics=hive.Pooling(hive.Decompress(pics),255)

r = [hive.Conv2d(pics, [np.load("ConvLayerFilter/ConvLayer2Filter" + str(x) + ".npy")],6, 1) for x in range(1, 17)]
pics = [Extension.NumpyAddExtension(hive.Decompress(r[x])) for x in range(16)]

pics=hive.Pooling(pics,255)

vector = hive.FullConnect(np.array(pics).flatten(),np.load('FullConnectLayer/FullConnectLayer1.npy'),255)

vector = hive.FullConnect(vector, np.load('FullConnectLayer/FullConnectLayer2.npy'))

vector = hive.FullConnect(vector, np.load('FullConnectLayer/FullConnectLayer3.npy'))

# 注意：权重是 filterReset.py 生成的未训练随机整数，这里的输出不是真正的识别结果
print("this number is : ",vector.argmax())
