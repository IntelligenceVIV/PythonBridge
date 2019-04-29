# @Time    : 2019/4/21 19:50
# @Author  : Noah
# @File    : simple factory pattern.py
# @Software: PyCharm
# @description: 允许接口创建对象但不会暴露对象的创建逻辑

# 创建型设计模式

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("B how B how")


class Cat(Animal):
    def do_say(self):
        print("M eow M eow")


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == "__main__":
    factory = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat? ")
    factory.make_sound(animal)
