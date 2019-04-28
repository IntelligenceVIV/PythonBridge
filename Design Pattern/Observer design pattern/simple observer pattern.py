# @Time    : 2019/4/21 21:26
# @Author  : Noah
# @File    : simple observer pattern.py
# @Software: PyCharm
# @description: 一个对象中的任何更改都将自动通知给其它依赖对象 并且封装主题的核心组件

class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

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

    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    subject.notifyAll('notification')