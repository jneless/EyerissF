import numpy as np


def Compress(NpArray, RateNeed=0):
    if NpArray.ndim == 1:
        Row = NpArray.shape
        Column = 1

    else:
        Row, Column = NpArray.shape

    ComedNpArray = np.array([Row, Column], dtype=int)

    # NpArray=NpArray.flatten()
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

    if RateNeed == 0:
        return ComedNpArray
    else:
        CompressRate = float(ComedNpArray.size) / (Row * Column)
        print("CompressRate is :",CompressRate)
        return ComedNpArray

def Decompress(NpArray):
    Length = NpArray.size - 2
    Row = NpArray[0]
    Column = NpArray[1]

    DecomedNpArray = list()

    for interr in range(Length):

        if NpArray[interr + 2] == 0:
            for x in range(NpArray[interr + 3]):
                DecomedNpArray.append(0)
        elif NpArray[interr + 1] == 0:  # NpArray[interr+2] != 0
            pass

        else:  # NpArray[interr+2] != 0 && NpArray[interr+1] != 0
            DecomedNpArray.append(NpArray[interr + 2])

    DecomedNpArray = np.array(DecomedNpArray, dtype=int)
    DecomedNpArray = DecomedNpArray.reshape(Row, Column)
    return DecomedNpArray

def CompressArray(array):
    assert type(array) == type(list())
    return [Compress(x) for x in array]

def DecompressArray(array):
    assert type(array) == type(list())
    return [Decompress(x) for x in array]


