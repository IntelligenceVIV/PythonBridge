# @Time    : 2019/4/21 21:26
# @Author  : Noah
# @File    : simple observer pattern.py
# @Software: PyCharm
# @description: 一个对象中的任何更改都将自动通知给其它依赖对象并且封装主题的核心组件

# 观察者模式 --- 了解对象的情况 => 属于行为型模式 ---主要关注的是对象的责任，处理对象之间的交互以实现更大的功能
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    # notify 通知
    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            # 调用观察对象 notify 方法
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'Form', subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


if __name__ == "__main__":
    subject = Subject()
    # 定义对象之间的一对多的依赖关系从而使得一个对象中任何更改都将自动通知给其他依赖对象
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    # 封装了主题的核心组件
    subject.notifyAll('notification')
