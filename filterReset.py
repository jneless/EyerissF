import numpy as np


def main():
    # 卷积层：第 1 层 6 个、第 2 层 16 个 5x5 卷积核
    for layer, count in ((1, 6), (2, 16)):
        for i in range(1, count + 1):
            x = np.random.randint(-5, 6, (5, 5), dtype=int)
            np.save(f"ConvLayerFilter/ConvLayer{layer}Filter{i}.npy", x)

    # 全连接层：400x120、120x84、84x10
    for i, shape in enumerate([(400, 120), (120, 84), (84, 10)], start=1):
        x = np.random.randint(-5, 6, shape, dtype=int)
        np.save(f"FullConnectLayer/FullConnectLayer{i}.npy", x)


if __name__ == "__main__":
    main()
