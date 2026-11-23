import matplotlib.pyplot as plt
import numpy as np
from IO2 import Decompress


def NumpyAddExtension(list):
    r = np.zeros(list[0].shape, dtype=int)
    for x in list:
        r = r + x
    return r

def PicSave(pic, name):
    # 1 张图：未压缩的输入图；6 或 16 张图：压缩后的特征图
    grids = {1: (1, 1), 6: (3, 2), 16: (4, 4)}
    if len(pic) not in grids:
        return
    fig, axes = plt.subplots(*grids[len(pic)], squeeze=False)
    for i, ax in enumerate(axes.flat):
        if len(pic) == 1:
            ax.imshow(pic[0]).set_cmap("gray")
            ax.set_title("Input pic")
        else:
            ax.imshow(Decompress(pic[i])).set_cmap("gray")
            ax.set_title("Map" + str(i + 1))
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
    plt.savefig(name, bbox_inches="tight")
    plt.close(fig)
