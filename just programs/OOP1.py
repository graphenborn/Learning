class Point3D:
    x = 1
    y = 6
    z = 17

    def getter(self):
        print(self.x, self.y, self.z, "\n")


a = Point3D()
b = Point3D()
c = Point3D()

print("Создаем экземпляр A")
a.getter()

print ("Меняем X в классе:")
Point3D.x = 7

a.getter()


print("Удаляем атрибут Z:")
delattr(Point3D, "z")

print(Point3D.__dict__, "\n")

print("Добавляем экземплярам A и B атрибут Z:")
a.z = 27
b.z = 32
a.getter()
b.getter()