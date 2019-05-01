# @Time    : 2019/4/18 2:55
# @Author  : Noah
# @File    : recursion.py
# @Software: PyCharm
# @description: recursion knowledge
def recursion(n):
    if n < 1:
        return -1

    elif n == 1 or n == 2:
        return 1

    else:
        return recursion(n - 1) + recursion(n - 2)


if __name__ == "__main__":
    result = recursion(30)
    if result != -1:
        print("result: {0}".format(result))  # result: 832040

#################################################################
# Recursion max depth
import sys

get_depth = sys.getrecursionlimit()
print("result: {0}".format(get_depth))  # result: 1000

# Set the recursion depth
set_depth = sys.setrecursionlimit(1200)


#################################################################
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)
        print(x, '-->', z)
        hanoi(n - 1, y, x, z)


n = int(input("please input the number of hanoi: "))
hanoi(n, 'X', 'Y', 'Z')

#################################################################