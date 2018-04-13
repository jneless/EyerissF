from EyerissF import EyerissF as EF
import numpy as np
import time

a=time.time()

ef=EF()
ef.InitPEs()

p=np.array([[4,3,1,0],
            [2,1,0,1],
            [1,2,4,1],
            [3,1,0,2]])

f=np.array([[1,0,1],
            [2,1,0],
            [0,0,1]])

r=ef.Conv2d(p,f)

b=time.time()

print(p)
print(f)
print(r)
print(b-a)