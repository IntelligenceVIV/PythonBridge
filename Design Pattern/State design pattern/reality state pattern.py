# @Time    : 2019/4/22 0:11
# @Author  : Noah
# @File    : reality state pattern.py
# @Software: PyCharm
# @description: 以计算机系统为例展示状态设计模式

class ComputerState(object):
    name = "state"
    allowed = []

    def swith(self, state):
        if state.name in self.allowed:
            print("Current:", self, ' => swithed to new state', state.name)
            self.__class__ = state
        else:
            print("Current:", self, ' => swithing to ', state.name, 'not possible.')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.swith(state)


if __name__ == "__main__":
    comp = Computer()
    comp.change(On)
    comp.change(Off)

    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)

    comp.change(On)
    comp.change(Off)
