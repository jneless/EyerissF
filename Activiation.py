import numpy as np
import math

def Relu(array):
    array[array<0]=0
    return array

def Sigmoid(array):
    for x in range(0,len(array)-1):
        array[x]=1.0 / (1 + math.exp(-array[x]))
    return array

if __name__ == '__main__':
    a=np.array(np.arange(-3,3),dtype=np.float32)
    b=Sigmoid(a)
    print(a)
    print(b)