# @Time    : 2019/4/18 2:41
# @Author  : Noah
# @File    : closure.py
# @Software: PyCharm
# @description: 闭包(内嵌函数可以访问外部函数作用域的值)

def funX(x):
    def funY(y):
        print("result: {0}".format(x + y))

    return funY(7)


if __name__ == "__main__":
    funX(3)

# result: 10
