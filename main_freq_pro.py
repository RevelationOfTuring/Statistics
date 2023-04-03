import random
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')


def toss():
    # 以50%的概率返回0或1
    return random.randint(0, 1)


if __name__ == '__main__':
    # 该次实验跑多少次硬币
    indices = []
    # 每一次正面朝上的频率
    freq = []
    # 分别抛10 ~ 10000次（步长为10）
    for toss_num in range(10, 10001, 10):
        heads = 0
        for _ in range(toss_num):
            if toss() == 0:
                heads += 1
        freq.append(heads / toss_num)
        indices.append(toss_num)
    plt.plot(indices, freq)
    plt.show()
