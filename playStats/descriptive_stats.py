from collections import Counter
from math import sqrt


### 集中趋势
def frequency(data):
    # 计算频率
    counter = Counter(data)
    ret = []
    for point in counter.most_common():
        # point[0]为数据，point[1]为对应频数
        ret.append((point[0], point[1] / len(data)))
    return ret


def mode(data):
    # 众数
    counter = Counter(data)
    # counter.most_common()的返回值是按照频数由高到低排列的，即counter.most_common()[0]就是出现最多的数据
    if counter.most_common()[0][1] == 1:
        # 说明众数不存在
        return None, None
    # 是否存在多个众数
    count = counter.most_common()[0][1]  # 众数的出现频数
    ret = []
    for point in counter.most_common():
        if point[1] == count:
            ret.append(point[0])
        else:
            break
    return ret, count


def median(data):
    """中位数"""
    sorted_data = sorted(data)  # 排序
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def mean(data):
    """均值"""
    return sum(data) / len(data)


### 离散趋势
def rng(data):
    """极差"""
    return max(data) - min(data)


def quartile(data):
    """四分位数"""
    n = len(data)
    q1, q2, q3 = None, None, None
    if n >= 4:
        sorted_data = sorted(data)
        # q2=中位数
        q2 = median(sorted_data)
        if n % 2 == 1:
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2 + 1:])
        else:
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2:])
    return q1, q2, q3


def variance(data):
    """方差"""
    n = len(data)
    if n <= 1:
        return None
    mean_value = mean(data)
    return sum((e - mean_value) ** 2 for e in data) / (n - 1)


def std(data):
    """标准差"""
    return sqrt(variance(data))
