import numpy as np

def Pooling(array,activation):
    assert isinstance(array, list)
    return [MAXPooling(x,activation) for x in array]

def MAXPooling(Array,activation=1, ksize=2):
    # 输入必须是二维数组，并且高和宽都是 ksize 的整数倍，否则池化窗口会错位
    if np.ndim(Array) != 2 or any(n % ksize for n in np.shape(Array)):
        raise ValueError(f"MAXPooling needs a 2-D array whose sides are multiples of ksize={ksize}, "
                         f"got shape {np.shape(Array)}")

    V2list = np.vsplit(Array, len(Array) // ksize)

    VerticalElements = list()
    HorizontalElements = list()

    for x in V2list:
        H2list = np.hsplit(x, len(x[0]) // ksize)
        HorizontalElements.clear()
        for y in H2list:
            # y should be a two-two square
            HorizontalElements.append(y.max())
        VerticalElements.append(np.array(HorizontalElements))

    return np.array(np.array(VerticalElements)/activation,dtype=int)
