# @Time    : 2019/4/21 20:38
# @Author  : Noah
# @File    : Implement the door pattern.py
# @Software: PyCharm
# @description: 解决如何用单个接口对象来表示复杂的子系统

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


class YouManger(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!")

    def askEventManager(self):
        print("You:: Let's Content the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


you = YouManger()
you.askEventManager()
