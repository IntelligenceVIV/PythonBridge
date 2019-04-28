# @Time    : 2019/4/21 21:00
# @Author  : Noah
# @File    : simple proxy pattern.py
# @Software: PyCharm
# @description: 控制对象访问

# 代理通常就是一个介于寻求方和提供方之间的中介系统
class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBusy


# 代理
class Agent(object):
    def __init__(self):
        # 主要 principal
        self.principal = None

    def work(self):
        # 发起方 => 提供方
        self.actor = Actor()
        # self.isBusy
        if self.actor.getStatus():
            # change isBusy state
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == "__main__":
    obj = Agent()
    obj.work()
