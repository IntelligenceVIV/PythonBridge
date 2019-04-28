# @Time    : 2019/4/21 0:49
# @Author  : Noah
# @File    : heap_sort.py
# @Software: PyCharm
# @description: python -m doctest -v heap_sort.py

# 利用堆这种数据结构所设计的一种排序算法
# 堆是一个近似完全二叉树的结构
# 并同时满足堆积的性质：
# 每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆
# 每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆


# heapify函数作用是将待排序序列构造成一个大顶堆，此时整个序列的最大值就是堆顶的根节点
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    '''
    Pure implementation of the heap sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    # >>> heap_sort([0, 5, 3, 2, 2])
    # [0, 2, 2, 3, 5]
    # >>> heap_sort([])
    # []
    # >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    '''
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    # 将堆顶元素与末尾元素进行交换，使末尾元素最大
    # 然后继续调整堆，再将堆顶元素与末尾元素交换得到第二大元素
    # 如此反复进行交换、重建、交换
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == "__main__":
    lst = [23, 17, 29, 10, 15, 12, 24, 19]
    sorted_lst = heap_sort(lst)
    print(sorted_lst)

# 再简单总结下堆排序的基本思路：
#
# 　　a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
#
# 　　b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
#
# 　　c.重新调整结构使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序
