from EyerissF import EyerissF as EF
import numpy as np
import time



ef=EF()

pic=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
pic2=np.hstack((pic,pic))

flt=np.array([[1,2],[3,4]])

print(ef.Conv2d(pic2,flt))