'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_r(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_c(self):
        return (self.radius ** 2) * 3.14

    def circumference(self):
        return 2 * 3.14 * self.radius


x = Rectangle(4, 2)
y = Circle(10)

print(x.area_r())


