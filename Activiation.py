def Relu(array):
    array[array < 0] = 0
    return array

def ReluArray(array):
    assert isinstance(array, list)
    return [Relu(x) for x in array]
