# @Time    : 2019/4/21 19:25
# @Author  : Noah
# @File    : metaclass and singleton.py
# @Software: PyCharm
# @description: 元类是一个类的类
class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("**** Here's My Int ****", args)
        print("Now do whatever you want with these objects....")
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)


########################################################################

class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)

########################################################################
