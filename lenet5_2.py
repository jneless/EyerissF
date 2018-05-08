from Compiler import Compiler
from EyerissF import EyerissF as EF
import IOCompression
import matplotlib.pyplot as plt
import skimage.io as io
from Pooling import *
from Extension import *




ef = EF()
cp = Compiler(ef)


Pic=[]
pic=io.imread("Pic/01.png",as_grey=True)
pic=255-pic
Pic.append(pic)

# PicSave(Pic,"Input.png")
# plt.imshow(pic)
# plt.show()

Flt=[]
flt1 = np.load('ConvLayerFilter/ConvLayer1Filter1.npy')
flt2 = np.load('ConvLayerFilter/ConvLayer1Filter2.npy')
flt3 = np.load('ConvLayerFilter/ConvLayer1Filter3.npy')
flt4 = np.load('ConvLayerFilter/ConvLayer1Filter4.npy')
flt5 = np.load('ConvLayerFilter/ConvLayer1Filter5.npy')
flt6 = np.load('ConvLayerFilter/ConvLayer1Filter6.npy')
Flt.append(flt1)
Flt.append(flt2)
Flt.append(flt3)
Flt.append(flt4)
Flt.append(flt5)
Flt.append(flt6)


#第一层

Pic= IOCompression.InputCompress(Pic)
Flt = IOCompression.InputCompress(Flt)
cp.input(Pic, Flt, 1, 6)
cp.Con2LogicalMapping()
cp.Con2PhysicalMapping()
cp.Conv2d()
cp.Reverse()
z=cp.GetReturnImgs()

# 6个28*28
# PicSave(z,"ConvLayer1.png")
# for x in z:
#     c=IOCompression.Decompress(x)
#     plt.imshow(c)
#     plt.show()




#第二层
z=Pooling(z)

# 6个14*14
# for x in z:
#     c=IOCompression.Decompress(x)
#     plt.imshow(c)
#     plt.show()


#第三层

z=IOCompression.DecompressArray(z)
r=[]

for x in range(1,17):

    Flt.clear()
    flt = np.load('ConvLayerFilter/ConvLayer2Filter'+str(x)+'.npy')
    Flt.append(flt)

    z=IOCompression.InputCompress(z)
    Flt=IOCompression.InputCompress(Flt)

    cp.input(z, Flt, 6, 1)
    cp.Con2LogicalMapping()
    cp.Con2PhysicalMapping()
    cp.Conv2d()
    cp.Reverse()

    r.append(cp.GetReturnImgs())

z=[NumpyAddExtension(DecompressArray(r[x])) for x in range(16)]
z=InputCompress(z)

# PicSave(z,"ConvLayer2.png")
# for x in z:
#     c=IOCompression.Decompress(x)
#     plt.imshow(c)
#     plt.show()


#第四层
z=Pooling(z)

# for x in z:
#     c=IOCompression.Decompress(x)
#     plt.imshow(c)
#     plt.show()


# 第五层

z=IOCompression.DecompressArray(z)
z=np.array(z)
z=z.flatten()

f1=np.load('FullConnectLayer/FullConnectLayer1.npy')
z=z.dot(f1)



#第六层

f2=np.load('FullConnectLayer/FullConnectLayer2.npy')
z=z.dot(f2)
z=np.array(z/255,dtype=int)

#第七层

f3=np.load('FullConnectLayer/FullConnectLayer3.npy')
z=z.dot(f3)

print("线性空间向量为：",z)

print("此数字是： " ,np.argmax(z))









