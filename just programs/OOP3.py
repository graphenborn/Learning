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

    def __checkValue(value):
        return isinstance(value, int)

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if RectValue.__checkValue(value):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError ("Координаты должны быть числами")


class Rectangle:
    
    x1 = RectValue()
    y1 = RectValue()
    x2 = RectValue()
    y2 = RectValue()

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2