# @Time    : 2019/4/21 19:20
# @Author  : Noah
# @File    : monostate singleton.py
# @Software: PyCharm
# @description: 所有实例对象共享相同状态

class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Borg()

d = Borg()

b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'd': ", d)
print("Borg State 'b': ", b.__dict__)
print("Borg State 'd': ", d.__dict__)
