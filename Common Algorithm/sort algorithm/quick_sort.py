# @Time    : 2019/4/21 0:47
# @Author  : Noah
# @File    : quick_sort.py
# @Software: PyCharm
# @description: python -m doctest -v quick_sort.py

# 根据二分法思想来用l[0]划分两个列表
def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    ARRAY_LENGTH = len(ARRAY)
    if (ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [element for element in ARRAY[1:] if element > PIVOT]
        LESSER = [element for element in ARRAY[1:] if element <= PIVOT]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
