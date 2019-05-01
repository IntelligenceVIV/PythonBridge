# @Time    : 2019/4/21 0:49
# @Author  : Noah
# @File    : radix_sort.py
# @Software: PyCharm
# @description: 基数排序

# 基数排序是桶排序的扩展
# 基本思想是：将整数按位数切割成不同的数字然后按每个位数分别比较
# 基数排序法属于稳定性的排序

def radixsort(lst):
    RADIX = 10
    placement = 1

    # get the maximum number
    max_digit = max(lst)

    while placement < max_digit:
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split lst between lists
        for i in lst:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        # empty lists into lst array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        # move to next
        placement *= RADIX

    return lst


if __name__ == "__main__":
    print(radixsort([12, 10, 9, 13, 20, 19, 27]))


# 总结：

# 将所有待比较数值统一为同样的数位长度，数位较短的数前面补零

# 然后从最低位开始（按照个、十和百位数顺序）依次进行一次排序

# 这样从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列