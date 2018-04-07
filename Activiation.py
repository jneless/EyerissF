import numpy as np
import math

def Relu(array):
    array[array<0]=0
    return array

def Sigmoid(array):
    return [1.0/(1 + math.exp(-x)) for x in array ]



if __name__ == '__main__':
    a=np.array(np.arange(-3,3),dtype=np.float32)
    c= Sigmoid(a)
    print("a:",a)