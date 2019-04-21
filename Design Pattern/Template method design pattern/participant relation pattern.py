# @Time    : 2019/4/21 22:32
# @Author  : Noah
# @File    : participant relation pattern.py
# @Software: PyCharm
# @description: 展示该模式中所有参与者的关系

from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operational1(self):
        pass

    @abstractmethod
    def operational2(self):
        pass

    def template_method(self):
        print("Defining the Algorithm. Operation1 follows Operation2")
        self.operational2()
        self.operational1()


class ConcreteClass(AbstractClass):
    def operational1(self):
        print("My Concrete Operation1")

    def operational2(self):
        print("Operation 2 remains same")


class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()


client = Client()
client.main()
