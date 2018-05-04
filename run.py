from Compiler import Compiler
from EyerissF import EyerissF
from Activiation import Relu
from IOCompression import *
import conf
cp=Compiler()

pic=np.ones((20,5),dtype=int)
flt=np.ones((5,5),dtype=int)




print(pic.shape)
print(flt.shape)
e = EyerissF()

t=list()
for x in cp.Con2PhysicalMapping(pic,flt,1,1):
    # a, b=e.__DataDeliver__(x,flt)
    # e.__run__()
    # e.__ShowStates__()
    # w=e.__PsumTransport__(a,b)
    w=e.Conv2d(x,flt,1,1)

    t.append(w)
    print(w)

print(np.vstack(t))




