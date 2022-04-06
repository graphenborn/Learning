class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_length(self):
        return self.x2-self.x1

    def get_width(self):
        return self.y1 - self.y2

    def get_area(self):
        return (self.x2-self.x1)*(self.y1 - self.y2)

    def get_perimeter(self):
        return ((self.x2-self.x1)+(self.y1 - self.y2))*2

    def is_square(self):
        return (self.x2-self.x1) == (self.y1 - self.y2)


class Square(Rectangle):

    def __init__(self, x, y, l):
        super().__init__(x-l, y, x, y-l)