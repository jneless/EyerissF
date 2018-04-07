import numpy as np
Pic1=np.array([[1,2],[3,4],[5,6],[7,8]])
Pic2=np.array([[9,10],[11,12],[13,14],[15,16]])

Pic=list()
Pic.append(Pic1)
Pic.append(Pic2)

def FmapReuse(Pictures,FilterWights=0):
    length=len(Pictures)
    l = list()
    line=list()
    for y in range(0, len(Pictures[0])):
        for x in range(0, length):
            l.append(Pictures[x][y])
        line.append(np.hstack(l))
        l.clear()
    c=np.array(line)
    return c

