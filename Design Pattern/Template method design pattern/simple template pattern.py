# @Time    : 2019/4/21 22:25
# @Author  : Noah
# @File    : simple template pattern.py
# @Software: PyCharm
# @description: 模板方法设计模式 --- 封装算法

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):

    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


# class
class iOSCompiler(Compiler):
    # method 1
    def collectSource(self):
        print("Collecting Swift Source Code")
    # method 2
    def compileToObject(self):
        print("Compiling Swift code to LLVM bit code")
    # method 3
    def run(self):
        print("Program run on runtime environment")


# instance
iOS = iOSCompiler()
# metaclass method
iOS.compileAndRun()
