from collections import Counter
from playStats.descriptive_stats import std, variance, frequency, mode, median, mean, rng, quartile

if __name__ == '__main__':
    data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    counter = Counter(data)
    # 计算频数
    print(counter.most_common())
    # 计算频率
    print(frequency(data))
    # 计算众数
    data = [2, 2, 2, 1, 1, 1, 3, 3]
    print(mode(data))
    print(mode([1, 2, 3]))
    print(mode([1, 2, 3, 3]))
    # 计算中位数
    print(median([1, 4, 2, 3]))
    print(median([1, 4, 2, 5, 3]))
    # 计算均值
    print(mean([1, 4, 2, 3, 5]))
    # 计算极差
    print(rng([1, 4, 2, 3, 3, 5]))
    # 计算四分位数
    print(quartile([1, 4, 2, 3, 5]))
    print(quartile([1, 4, 2, 3, 5, 8]))
    # 计算方差
    print(variance([1, 4, 2, 3, 5, 8]))
    # 计算标准差
    print(std([1, 4, 2, 3, 5, 8]))
