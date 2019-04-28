# @Time    : 2019/4/21 0:51
# @Author  : Noah
# @File    : shell_sort.py
# @Software: PyCharm
# @description: python -m doctest -v shell_sort.py

# 希尔排序(增量递减排序)
# 基本思路是把原来的序列等效视为一个矩阵的形式
# 矩阵的列数也称为宽度或者增量(w)
# 当w = 1时就是插入排序过程

# 初期选用大跨步（增量较大）间隔比较，使记录跳跃式接近它的排序位置
# 然后增量缩小；最后增量为 1 ，这样记录移动次数大大减少，提高了排序效率
# 希尔排序对增量序列的选择没有严格规定

def shell_sort(collection):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending
    # >>> shell_sort([0, 5, 3, 2, 2])
    # [0, 2, 2, 3, 5]
    # >>> shell_sort([])
    # []
    # >>> shell_sort([-2, -5, -45])
    # [-45, -5, -2]
    """
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    return collection


if __name__ == "__main__":
    l = [23, 35, 18, 34, 27, 19]
    sort_l = shell_sort(l)
    print(sort_l)
