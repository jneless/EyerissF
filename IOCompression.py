import numpy as np


def Compress(NpArray, RateNeed=0):
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
        return ComedNpArray, CompressRate


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

    DecomedNpArray = np.array(DecomedNpArray,dtype=int)
    DecomedNpArray = DecomedNpArray.reshape(Row, Column)
    return DecomedNpArray


if __name__ == "__main__":
    NpArray = np.array(
        [[0, 0, 0, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0]]
    )
    print("压缩前：\n", NpArray)
    c = Compress(NpArray)
    print("压缩后\n", c)
    c = Decompress(c)
    print("解压后\n", c)
