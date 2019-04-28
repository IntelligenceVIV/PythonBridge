# @Time    : 2019/4/21 0:48
# @Author  : Noah
# @File    : cocktail_shaker_sort.py
# @Software: PyCharm
# @description: 鸡尾酒排序

# 是冒泡排序的一种变形又称双向冒泡排序
# 该算法与冒泡排序的不同处在于排序时是以双向在序列中进行排序

def cocktail_shaker_sort(unsorted):
    """
    Pure implementation of the cocktail shaker sort algorithm in Python.
    """
    for i in range(len(unsorted) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                swapped = True

        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True

        if not swapped:
            return unsorted


if __name__ == '__main__':
    print(cocktail_shaker_sort([10, 9, 14, 19, 15, 9, 21]))
