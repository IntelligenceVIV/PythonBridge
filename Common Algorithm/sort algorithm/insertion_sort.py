# @Time    : 2019/4/21 0:33
# @Author  : Noah
# @File    : insertion_sort.py
# @Software: PyCharm
# @description: python -m doctest -v insertion_sort.py

def insertion_sort(collection):
    """Pure implementation of the insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort([])
    []
    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    for index in range(1, len(collection)):
        while index > 0 and collection[index - 1] > collection[index]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection