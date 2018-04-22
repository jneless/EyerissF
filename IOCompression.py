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

    DecomedNpArray = np.array(DecomedNpArray)
    DecomedNpArray = DecomedNpArray.reshape(Row, Column)
    return DecomedNpArray


if __name__ == "__main__":
    NpArray = np.array(
        [[0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0]])
    print(NpArray)
    c = Compress(NpArray)
    print(c)
    c = Decompress(c)
    print(c)
