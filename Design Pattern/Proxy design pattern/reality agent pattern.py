# @Time    : 2019/4/21 21:08
# @Author  : Noah
# @File    : reality agent pattern.py
# @Software: PyCharm
# @description: 通过付款用例来展示代理模式的实用场景
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True

        else:
            print("Bank:: Sorry, not enough funds")
            return False


class DebitCard(Payment):
    def __init__(self):
        # 银行类 => 对象实例化
        self.bank = Bank()

    def do_pay(self):
        # 处理用户请求
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


class You:
    def __init__(self):
        print("You:: Lets buy the Denim shirt")
        # 借记卡类 => 对象实例化
        self.debitCard = DebitCard()
        self.isPurchased = None

    # 内部逻辑调用
    def make_payment(self):
        # 调用对象 do_pay 方法 => 处理用户支付的请求
        self.isPurchased = self.debitCard.do_pay()

    # 最后执行删除操作
    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")


if __name__ == "__main__":
    you = You()
    you.make_payment()
