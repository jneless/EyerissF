from Compiler import Compiler
from EyerissF import EyerissF
from Activiation import Relu
from IOCompression import *
import conf
cp=Compiler()

pic=np.ones((20,5))
flt=np.ones((5,5))

e = EyerissF()
e.InitPEs()

t=list()
for x in cp.Con2PhysicalMapping(pic,flt):
    a, b=e.__DataDeliver__(x,flt)
    e.__run__()
    e.__ShowStates__()
    w=e.__PsumTransport__(a,b)
    e.__SetALLPEsState__(conf.ClockGate)
    t.append(w)
    print(w)

print(np.vstack(t))




