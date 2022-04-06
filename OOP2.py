class Point3D:
    
    def __init__(self, x = 0, y = 0, z = 0):
        self.coords = [x, y, z]


    def setter(self, x, y, z):
        self.coords = [x, y, z]


    def getter(self):
        print(tuple(self.coords))

class Point():
    def __init__(self, obj=None):
        if obj:
            self.x = obj.x
            self.y = obj.y
        else:
            self.x = 0
            self.y = 0

    def get(self):
        return self.x, self.y


class Points:

    list = []

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Points.list.append(self)

d = input("введите количество точек: ")
aboba = [i for i in range(int(d))]

for i in range (len(aboba)):
    x, y = input(f"Введите координаты точки {i+1}: ").split()
    aboba[i] = Points(x, y)

for i in range (len(Points.list)):
    print(f"x = {Points.list[i].x} y = {Points.list[i].y}")