# @Time    : 2019/4/21 20:38
# @Author  : Noah
# @File    : Implement the door pattern.py
# @Software: PyCharm
# @description: 门面模式 --- 与门面相适

# 结构设计模式
# 它为子系统中的一组接口提供一个统一的接口
# 解决如何用单个接口对象来表示复杂的子系统
# 它促进了实现与多个客户端的解耦

# 门面facade通常指事物的表面

# 门面隐藏内部系统复杂性的同时为客户提供一个接口以便它们可以非常轻松地访问系统


########################################################################

# 根据应用场景提供多个子系统
class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")


class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        print('Chinese & Continental Cuisine to be served\n\n')


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")


########################################################################

# 门面 facade 角色
class EventManager(object):
    def __init__(self):
        print("Event Manger:: Let me talk to the folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


########################################################################

# 管理员角色
class YouManger(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!")

    def askEventManager(self):
        print("You:: Let's Content the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


if __name__ == "__main__":
    you = YouManger()
    you.askEventManager()

########################################################################
