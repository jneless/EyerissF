import numpy as np

def Pooling(array,activation):
    assert type(array) == type(list())
    return [MAXPooling(x,activation) for x in array]

def MAXPooling(Array,activation=1, ksize=2):
    assert len(Array) % ksize == 0

    V2list = np.vsplit(Array, len(Array) / ksize)

    VerticalElements = list()
    HorizontalElements = list()

    for x in V2list:
        H2list = np.hsplit(x, len(x[0]) / ksize)
        HorizontalElements.clear()
        for y in H2list:
            # y should be a two-two square
            HorizontalElements.append(y.max())
        VerticalElements.append(np.array(HorizontalElements))

    return np.array(np.array(VerticalElements)/activation,dtype=int)
