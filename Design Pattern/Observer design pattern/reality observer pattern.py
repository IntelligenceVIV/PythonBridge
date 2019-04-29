# @Time    : 2019/4/21 21:36
# @Author  : Noah
# @File    : reality observer pattern.py
# @Software: PyCharm
# @description: 通过新闻机构来展示观察者模式

from abc import ABCMeta, abstractmethod

# 抽象类
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

######################################################################

# 主题 => 提供用户使用的接口
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    # 供观察者来注册
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    # 注销
    def detach(self):
        return self.__subscribers.pop()

    # 返回已经使用主题Subject注册的所有订户的列表
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    # 遍历已向NewsPublisher注册的所有订户
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    # 创建新消息
    def addNews(self, news):
        self.__latestNews = news

    # 返回最新消息
    def getNews(self):
        return "Got News:", self.__latestNews

######################################################################

# 观察者接口
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

# 用来演示Observers与Subject的松散耦合关系
class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

######################################################################
# 展示主题与观察者之间的交互
if __name__ == "__main__":
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("\nSubscribers: ", news_publisher.subscribers())
    news_publisher.addNews('Hello World')
    news_publisher.notifySubscribers()

    print("\nDetached: ", type(news_publisher.detach()).__name__)
    print("\nSubscribers: ", news_publisher.subscribers())

    news_publisher.addNews("My second news!")
    news_publisher.notifySubscribers()
