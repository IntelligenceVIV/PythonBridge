# @Time    : 2019/4/29 13:05
# @Author  : Noah
# @File    : command process pattern.py
# @Software: PyCharm
# @description: 

from abc import ABCMeta, abstractmethod


# Command 声明执行操作的接口
class Command(metaclass=ABCMeta):

    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        pass

# ConcreteCommand 将一个Receiver对象和一个操作绑定在一起
class ConcreteCommand(Command):

    def execute(self):
        self.recv.action()

# Receiver 知道如何实施与执行一个请求相关的操作
class Receiver:
    def action(self):
        print("Receiver Action")


# Invoker 要求该ConcreteCommand执行这个请求
class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


# Client 创建ConcreteCommand对象并设定其接收者
if __name__ == "__main__":
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
