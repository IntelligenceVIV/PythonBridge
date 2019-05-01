# @Time    : 2019/4/21 0:48
# @Author  : Noah
# @File    : bucket_sort.py
# @Software: PyCharm
# @description: 桶排序

import math


# 调用插入排序
def insertion_sort(collection):
    for index in range(1, len(collection)):
        while index > 0 and collection[index - 1] > collection[index]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection


# 默认桶的数量
DEFAULT_BUCKET_SIZE = 5


def bucketSort(myList, bucketSize=DEFAULT_BUCKET_SIZE):
    if (len(myList) == 0):
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        if myList[i] < minValue:
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[math.floor((myList[i] - minValue) / bucketSize)].append(myList[i])

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])

    return sortedArray


if __name__ == '__main__':
    sortedArray = bucketSort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sortedArray)

# 总结：

# 工作的原理是将数组分到有限数量的桶里

# 每个桶再个别排序（再使用别的排序算法或以递归方式继续进行排序）

# 最后依次把各个桶中的元素取出来得到最后有序序列