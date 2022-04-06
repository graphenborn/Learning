class Point():
    def __init__(self, x = 0.0, y = 0.0):
        self._x = float(x)
        self._y = float(y)

    def set(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = float(x)
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = float(y)