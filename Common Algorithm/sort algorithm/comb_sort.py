# @Time    : 2019/4/28 14:26
# @Author  : Noah
# @File    : comb_sort.py
# @Software: PyCharm
# @description: 梳排序

def comb_sort(data):
    """Pure implementation of comb sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    # >>> comb_sort([0, 5, 3, 2, 2])
    # [0, 2, 2, 3, 5]
    # >>> comb_sort([])
    # []
    # >>> comb_sort([-2, -5, -45])
    # [-45, -5, -2]
    """
    shrink_factor = 1.3
    gap = len(data)
    swapped = True
    # i = 0

    while gap > 1 or swapped:
        # Update the gap value for a next comb
        # 先定义一个步长该步长为数组的长度除以1.3
        gap = int(float(gap) / shrink_factor)

        swapped = False
        i = 0
        # 然后从第0个元素开始跟距离当前元素为步长大小的元素进行比较
        while gap + i < len(data):
            if data[i] > data[i + gap]:
                # Swap values
                data[i], data[i + gap] = data[i + gap], data[i]
                swapped = True
            i += 1

    return data


if __name__ == '__main__':
    unsorted = [0, 5, 3, 2, 2]
    print(comb_sort(unsorted))
