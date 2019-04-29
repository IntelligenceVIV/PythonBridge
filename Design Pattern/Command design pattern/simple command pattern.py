# @Time    : 2019/4/21 22:04
# @Author  : Noah
# @File    : simple command pattern.py
# @Software: PyCharm
# @description: 对象封装调用一个事件所需的全部信息

# 行为模式侧重于对象的响应性

# 命令模式 --- 封装调用

# Command Receiver Invoker Client

# 主要意图如下：
# 将请求封装为对象
# 可用不同的请求对客户进行参数化
# 允许将请求保存在队列中
# 提供面向对象的回调


# 在客户端代码中创建Wizard对象
class Wizard():
    def __init__(self, src, dir):
        self.choices = []
        self.dir = dir
        self.src = src

    # 存储用户能做出的选择
    def preferences(self, command):
        self.choices.append(command)

    # 会根据首选项来操作
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.dir)

            else:
                print("No Operation")


if __name__ == "__main__":
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
