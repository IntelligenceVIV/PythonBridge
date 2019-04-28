# @Time    : 2019/4/21 19:09
# @Author  : Noah
# @File    : classic singleton.py
# @Software: PyCharm
# @description: 只允许类生成一个对象并且重复提供同一个对象
class Singleton(object):
    def __new__(cls):
        # cls has instance attribute => only one equally cls
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()

print("Object Created: ", s)

v = Singleton()

print("Object Created: ", v)
