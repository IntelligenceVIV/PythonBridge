# @Time    : 2019/4/3 19:07
# @Author  : Noah
# @File    : 1.py
# @Software: PyCharm
# @description: 装饰器的简单应用
import functools


def login(text):
    def wrapper(fn):
        @functools.wraps(fn)
        def user():
            print(' '.join([text, fn()]))

        return user

    return wrapper


@login('Hello')
def main():
    return "World"


if __name__ == "__main__":
    main()
