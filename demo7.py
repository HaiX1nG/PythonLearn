class Shape:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

    def getArea(self):
        return self.length * self.width


rectangle = Rectangle("红色", 5, 3)
print("颜色:", rectangle.getColor())
print("周长:", rectangle.getPerimeter())
print("面积:", rectangle.getArea())

rectangle.setColor("蓝色")
print("颜色:", rectangle.getColor())
