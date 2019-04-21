# @Time    : 2019/4/21 23:55
# @Author  : Noah
# @File    : simple state pattern.py
# @Software: PyCharm
# @description: 关注的是对象的响应性

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def Handler(self):
        pass


class ConcreteStateB(State):
    def Handler(self):
        print("ConcreteStateB")


class ConcreteStateA(State):
    def Handler(self):
        print("ConcreteStateA")


class Context(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def Handler(self):
        self.state.Handler()


context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()
context.setState(stateA)
context.Handler()
