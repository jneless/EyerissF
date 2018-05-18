from Hive import Hive
from EyerissF import EyerissF as EF
import numpy as np
import Extension
import skimage.io as io
import matplotlib.pyplot as plt


ef = EF()
hive = Hive(ef,mode="manuel")

pics = [255-io.imread("Pic/01.png", as_grey=True)]
flts = [np.load("ConvLayerFilter/ConvLayer1Filter"+str(x)+".npy") for x in range(1,7)]

pics=hive.Compress(pics)
flts=hive.Compress(flts)

hive.input(pics, flts, 1, 6)
hive.Conv2LogicalMapping()
hive.Conv2PhysicalMapping()
hive.Conv2d()


hive.Reverse()
pics=hive.Output()

