class Calendar:

    __slots__ = ('__day', '__month', '__year')

    def __checkValue(x): return isinstance(x, int)

    def __init__(self, day, month, year):
        for i in [day, month, year]:
            if Calendar.__checkValue(i):
                self.__day = day
                self.__month = month
                self.__year = year
            else:
                raise AttributeError ("Неверный формат даты")

    def setDate(self, day, month, year):
        for i in [day, month, year]:
            if Calendar.__checkValue(i):
                self.__day = day
                self.__month = month
                self.__year = year
            else:
                raise AttributeError ("Неверный формат даты")

    def getDate(self):
        return self.__day, self.__month, self.__year


class RectValue:
    def __get__(instance, owner):
        return instance.__value

    def __set__(instance, value):
        instance.__value = value


class Rectangle:
    
    __tLX = RectValue()
    __tLY = RectValue()
    __bRX = RectValue()
    __bRY = RectValue()



class People:
    pass


class Man(People):
    def get_sex():
        return 'm'
        
class Woman(People):
    def get_sex():
        return 'w'



print(Woman.get_sex())