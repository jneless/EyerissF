import numpy as np


def Compress(NpArray):

    Row, Column = NpArray.shape
    ComedNpArray = np.array([Row, Column], dtype=int)
    NpArray = NpArray.reshape((1, Row * Column))
    ZeroCounter = 0

    for iterr in range(NpArray.size):

        if NpArray[0][iterr] == 0:
            ZeroCounter = ZeroCounter + 1
        else:
            if ZeroCounter == 0:
                ComedNpArray = np.append(ComedNpArray, np.array(NpArray[0, iterr]))
            else:
                ComedNpArray = np.append(ComedNpArray, np.array([0, ZeroCounter, NpArray[0, iterr]]))
                ZeroCounter = 0

    if ZeroCounter != 0:
        ComedNpArray = np.append(ComedNpArray, np.array([0, ZeroCounter]))

    return ComedNpArray

def Decompress():
    pass

if __name__=="__main__":
    NpArray = np.array([[0,0,0,1,1,1,0,0],[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0]])
    print(Compress(NpArray))