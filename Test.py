from Compiler import Compiler
from EyerissF import EyerissF as EF
import IOCompression
from Extension import *


ef = EF()
cp = Compiler(ef)

Pic = []
pic = np.random.randint(1,10,(8,8),dtype=int)
Pic.append(pic)
print(pic)

Flt=[]
flt1=np.ones((2,2),dtype=int)
flt2=np.ones((2,2),dtype=int)
flt2=flt2+flt1

Flt.append(flt1)
Flt.append(flt2)

Pic = IOCompression.InputCompress(Pic)
Flt = IOCompression.InputCompress(Flt)

print(Pic)
print(Flt)


cp.input(Pic, Flt, 1, 2)
cp.Con2LogicalMapping()
cp.Con2PhysicalMapping()
cp.Conv2d()

cp.Reverse()
z = cp.GetReturnImgs()

for x in z:
    print(z)





