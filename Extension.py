import numpy as np
import matplotlib.pyplot as plt
from IOCompression import *

def NumpyAddExtension(list):
    r = np.zeros(list[0].shape, dtype=int)
    for x in range(len(list)):
        r = r + list[x]
    return r


def PicSave(pic, name):
    if len(pic) == 1:

        fig0, ax0 = plt.subplots(nrows=1, ncols=1)
        ax0.imshow(pic[0]).set_cmap("gray")
        ax0.set_title("Input pic")
        ax0.get_xaxis().set_ticks([])
        ax0.get_yaxis().set_ticks([])
        plt.savefig(name, bbox_inches="tight")
        plt.close(fig0)

    elif len(pic) == 6:

        fig1, ax1 = plt.subplots(nrows=3, ncols=2)
        ax1[0, 0].imshow(Decompress(pic[0])).set_cmap("gray")
        ax1[0, 0].set_title("Map1")
        ax1[0, 0].get_xaxis().set_ticks([])
        ax1[0, 0].get_yaxis().set_ticks([])

        ax1[0, 1].imshow(Decompress(pic[1])).set_cmap("gray")
        ax1[0, 1].set_title("Map2")
        ax1[0, 1].get_xaxis().set_ticks([])
        ax1[0, 1].get_yaxis().set_ticks([])

        ax1[1, 0].imshow(Decompress(pic[2])).set_cmap("gray")
        ax1[1, 0].set_title("Map3")
        ax1[1, 0].get_xaxis().set_ticks([])
        ax1[1, 0].get_yaxis().set_ticks([])

        ax1[1, 1].imshow(Decompress(pic[3])).set_cmap("gray")
        ax1[1, 1].set_title("Map4")
        ax1[1, 1].get_xaxis().set_ticks([])
        ax1[1, 1].get_yaxis().set_ticks([])

        ax1[2, 0].imshow(Decompress(pic[4])).set_cmap("gray")
        ax1[2, 0].set_title("Map5")
        ax1[2, 0].get_xaxis().set_ticks([])
        ax1[2, 0].get_yaxis().set_ticks([])

        ax1[2, 1].imshow(Decompress(pic[5])).set_cmap("gray")
        ax1[2, 1].set_title("Map6")
        ax1[2, 1].get_xaxis().set_ticks([])
        ax1[2, 1].get_yaxis().set_ticks([])

        plt.savefig(name, bbox_inches="tight")
        plt.close(fig1)

    elif len(pic) == 16:

        fig1, ax1 = plt.subplots(nrows=4, ncols=4)
        ax1[0, 0].imshow(Decompress(pic[0])).set_cmap("gray")
        ax1[0, 0].set_title("Map1")
        ax1[0, 0].get_xaxis().set_ticks([])
        ax1[0, 0].get_yaxis().set_ticks([])

        ax1[0, 1].imshow(Decompress(pic[1])).set_cmap("gray")
        ax1[0, 1].set_title("Map2")
        ax1[0, 1].get_xaxis().set_ticks([])
        ax1[0, 1].get_yaxis().set_ticks([])

        ax1[0, 2].imshow(Decompress(pic[2])).set_cmap("gray")
        ax1[0, 2].set_title("Map3")
        ax1[0, 2].get_xaxis().set_ticks([])
        ax1[0, 2].get_yaxis().set_ticks([])

        ax1[0, 3].imshow(Decompress(pic[3])).set_cmap("gray")
        ax1[0, 3].set_title("Map4")
        ax1[0, 3].get_xaxis().set_ticks([])
        ax1[0, 3].get_yaxis().set_ticks([])

        ax1[1, 0].imshow(Decompress(pic[4])).set_cmap("gray")
        ax1[1, 0].set_title("Map5")
        ax1[1, 0].get_xaxis().set_ticks([])
        ax1[1, 0].get_yaxis().set_ticks([])

        ax1[1, 1].imshow(Decompress(pic[5])).set_cmap("gray")
        ax1[1, 1].set_title("Map6")
        ax1[1, 1].get_xaxis().set_ticks([])
        ax1[1, 1].get_yaxis().set_ticks([])

        ax1[1, 2].imshow(Decompress(pic[6])).set_cmap("gray")
        ax1[1, 2].set_title("Map7")
        ax1[1, 2].get_xaxis().set_ticks([])
        ax1[1, 2].get_yaxis().set_ticks([])

        ax1[1, 3].imshow(Decompress(pic[7])).set_cmap("gray")
        ax1[1, 3].set_title("Map8")
        ax1[1, 3].get_xaxis().set_ticks([])
        ax1[1, 3].get_yaxis().set_ticks([])

        #

        ax1[2, 0].imshow(Decompress(pic[8])).set_cmap("gray")
        ax1[2, 0].set_title("Map9")
        ax1[2, 0].get_xaxis().set_ticks([])
        ax1[2, 0].get_yaxis().set_ticks([])

        ax1[2, 1].imshow(Decompress(pic[9])).set_cmap("gray")
        ax1[2, 1].set_title("Map10")
        ax1[2, 1].get_xaxis().set_ticks([])
        ax1[2, 1].get_yaxis().set_ticks([])

        ax1[2, 2].imshow(Decompress(pic[10])).set_cmap("gray")
        ax1[2, 2].set_title("Map11")
        ax1[2, 2].get_xaxis().set_ticks([])
        ax1[2, 2].get_yaxis().set_ticks([])

        ax1[2, 3].imshow(Decompress(pic[11])).set_cmap("gray")
        ax1[2, 3].set_title("Map12")
        ax1[2, 3].get_xaxis().set_ticks([])
        ax1[2, 3].get_yaxis().set_ticks([])

        ax1[3, 0].imshow(Decompress(pic[12])).set_cmap("gray")
        ax1[3, 0].set_title("Map13")
        ax1[3, 0].get_xaxis().set_ticks([])
        ax1[3, 0].get_yaxis().set_ticks([])

        ax1[3, 1].imshow(Decompress(pic[13])).set_cmap("gray")
        ax1[3, 1].set_title("Map14")
        ax1[3, 1].get_xaxis().set_ticks([])
        ax1[3, 1].get_yaxis().set_ticks([])

        ax1[3, 2].imshow(Decompress(pic[14])).set_cmap("gray")
        ax1[3, 2].set_title("Map15")
        ax1[3, 2].get_xaxis().set_ticks([])
        ax1[3, 2].get_yaxis().set_ticks([])

        ax1[3, 3].imshow(Decompress(pic[15])).set_cmap("gray")
        ax1[3, 3].set_title("Map16")
        ax1[3, 3].get_xaxis().set_ticks([])
        ax1[3, 3].get_yaxis().set_ticks([])

        plt.savefig(name, bbox_inches="tight")
        plt.close(fig1)
