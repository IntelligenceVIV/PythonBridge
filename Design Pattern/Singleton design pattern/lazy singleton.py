# @Time    : 2019/4/21 19:14
# @Author  : Noah
# @File    : lazy singleton.py
# @Software: PyCharm
# @description: 能够确保在实际需要时才会创建对象

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()

print("Object Created: ", Singleton.getInstance())

v = Singleton()
