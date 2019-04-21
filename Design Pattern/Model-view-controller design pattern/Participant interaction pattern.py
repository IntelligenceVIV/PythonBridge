# @Time    : 2019/4/21 23:12
# @Author  : Noah
# @File    : Participant interaction pattern.py
# @Software: PyCharm
# @description: 展示该模式中所有参与者的交互情况

class Model(object):
    def logic(self):
        data = 'Got it!'
        print("Model: Crunchung data as per business logic")
        return data


class View(object):
    def update(self, data):
        print("View: Updating the view with results: ", data)


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller: Relayed the Client asks")
        data = self.model.logic()
        self.view.update(data)


class Client(object):
    print("Client: asks for certain information")
    controller = Controller()
    controller.interface()
