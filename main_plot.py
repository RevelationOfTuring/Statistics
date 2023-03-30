import matplotlib.pyplot as plt
import warnings
import random
from collections import Counter

warnings.filterwarnings('ignore')

if __name__ == '__main__':
    # scatter plot
    random.seed(666)
    # 生成100个0-100之间的整数
    x = [random.randint(0, 100) for _ in range(100)]
    y = [random.randint(0, 100) for _ in range(100)]
    plt.scatter(x, y)
    plt.show()

    # line plot 折线图（1维）
    x = [random.randint(0, 100) for _ in range(100)]
    plt.plot(range(100), x)
    plt.show()

    # bar plot 条形图（为分类变量服务）
    data = [3, 3, 4, 1, 5, 4, 2, 1, 5, 4, 4, 4, 5, 3, 2, 1, 4, 5, 5]
    counter = Counter(data)
    x = [point[0] for point in counter.most_common()]
    # y为各个观察值的频数
    y = [point[1] for point in counter.most_common()]
    plt.bar(x, y)
    plt.show()

    # histogram 直方图（为数值变量服务）
    data = [random.randint(1, 100) for _ in range(1000)]
    plt.hist(data, bins=15, rwidth=0.9)  # rwidth=0.9表示直方图bar和bar之间存在空白，rwidth越小，空白越大。 bins表示多少个柱形
    # plt.hist(data, bins=15, rwidth=0.8, density=True)  # density=True表示绘制的是频率直方图
    plt.show()

    # box plot
    plt.boxplot(data)
    plt.show()
    # 加入极端值
    data.append(200)
    data.append(-201)
    plt.boxplot(data)  # 能将极端值画出
    plt.show()

    # 并排箱线图
    data1 = [random.randint(66, 166) for _ in range(200)]
    data2 = [random.randint(60, 120) for _ in range(200)]
    plt.boxplot([data1, data2])
    plt.show()
