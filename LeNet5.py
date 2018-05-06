import numpy as np
from EyerissF import EyerissF as EF
from Compiler import Compiler as CP
from Pooling import  MAXPooling
import time
s=time.time()


ConvLayer1Filter1=np.load('ConvLayerFilter/ConvLayer1Filter1.npy')
ConvLayer1Filter2=np.load('ConvLayerFilter/ConvLayer1Filter2.npy')
ConvLayer1Filter3=np.load('ConvLayerFilter/ConvLayer1Filter3.npy')
ConvLayer1Filter4=np.load('ConvLayerFilter/ConvLayer1Filter4.npy')
ConvLayer1Filter5=np.load('ConvLayerFilter/ConvLayer1Filter5.npy')
ConvLayer1Filter6=np.load('ConvLayerFilter/ConvLayer1Filter6.npy')

ef=EF()
print("Eyeriss启动")

cp=CP()
print("驱动加载完成")

pic=np.load('pic/pic.npy')
print("输入图片尺寸",pic.shape)

Picture, FilterWeight,PictureNum,FilterWeightNum=cp.Con2LogicalMapping(pic[np.newaxis],FilterWeights=(ConvLayer1Filter1,ConvLayer1Filter2,
	ConvLayer1Filter3,ConvLayer1Filter4,ConvLayer1Filter5,ConvLayer1Filter6))

t=list()

#map是eyeriss每次实际处理的形状

map,ImageNum,FilterWeightNum=cp.Con2PhysicalMapping(Picture[0], FilterWeight,PictureNum,FilterWeightNum)
print("输入图片数量：",ImageNum,"输入卷积核数量：",FilterWeightNum)
print("重用方式 ： Fmap重用")



for x in map:
    w=ef.Conv2d(x,FilterWeight,ImageNum,FilterWeightNum)
    t.append(w)

bb=np.vstack(t)




print("卷积后整体尺寸 :",bb.shape)


x=cp.ReverseFmapReuse(bb,6)

n=0
for y in x :
    n=n+1
    print("第",n,"个卷积后的图片尺寸为 :",y.shape)

for y in range(len(x)):
    x[y]=MAXPooling(x[y])

n=0
for y in x :
    n = n + 1
    print("第",n,"个图片池化后尺寸为 :",y.shape)


print("二层卷积 + 池化")
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


flt=[]

flt.append(ConvLayer2Filter1)
flt.append(ConvLayer2Filter2)
flt.append(ConvLayer2Filter3)
flt.append(ConvLayer2Filter4)
flt.append(ConvLayer2Filter5)
flt.append(ConvLayer2Filter6)
flt.append(ConvLayer2Filter7)
flt.append(ConvLayer2Filter8)
flt.append(ConvLayer2Filter9)
flt.append(ConvLayer2Filter10)
flt.append(ConvLayer2Filter11)
flt.append(ConvLayer2Filter12)
flt.append(ConvLayer2Filter13)
flt.append(ConvLayer2Filter14)
flt.append(ConvLayer2Filter15)
flt.append(ConvLayer2Filter16)

pic=x[0]

FilterWeights=flt
Picture, FilterWeight,PictureNum,FilterWeightNum=cp.Con2LogicalMapping(pic[np.newaxis],FilterWeights)




t=list()

#map是eyeriss每次实际处理的形状

map,ImageNum,FilterWeightNum=cp.Con2PhysicalMapping(Picture[0], FilterWeight[np.newaxis],PictureNum,FilterWeightNum)

print("输入图片数量：",ImageNum,"输入卷积核数量：",FilterWeightNum)
print("重用方式 ： Fmap重用")



for x in map:
    w=ef.Conv2d(x,FilterWeight,ImageNum,FilterWeightNum)
    t.append(w)

bb=np.vstack(t)




print("卷积后整体尺寸 :",bb.shape)

x=cp.ReverseFmapReuse(bb,16)



n=0
for y in x :
    n=n+1
    print("第",n,"个卷积后的图片尺寸为 :",y.shape)

for y in range(len(x)):
    x[y]=MAXPooling(x[y])

n=0
for y in x :
    n = n + 1
    print("第",n,"个图片池化后尺寸为 :",y.shape)

arr=[]

for y in x :

    arr.append(np.reshape(y,(1,y.size)))

arr=np.array(arr)
arr=arr.reshape(1,arr.size)


f1=np.load('FullConnectLayer/FullConnectLayer1.npy')
arr=arr.dot(f1)
print("第一层全链接后尺寸为：",arr.shape)

f2=np.load('FullConnectLayer/FullConnectLayer2.npy')
arr=arr.dot(f2)
print("第二层全链接后尺寸为：",arr.shape)

f3=np.load('FullConnectLayer/FullConnectLayer3.npy')
arr=arr.dot(f3)
print("第三层softmax为：",arr.shape)

print("线性空间向量为：",arr,"(测试结构filter参数全为0)")

s2=time.time()

print("运行用时:",s2-s)

