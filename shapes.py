import math
class Shapes:
    def getArea(self):
        return None
    def getPerimeter(self):
        return None
class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return (self.width + self.height) * 2
    def getWidth(self):
        return self.width
    def setWidth(self, width):
        self.width = width
    def getHeight(self):
        return self.height
    def setHeight(self, height):
        self.height = height
class Square(Rectangle):
    def __init__(self, width):
        super.__init__(width, 1)
    def getPerimeter(self):
        return self.width * 4
    def getHeight(self):
        return self.getWidth(self)
    def setHeight(self, height):
        self.setWidth(height)
class Triangle(Shapes):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def getArea(self):
        return self.side1 + self.side2 + self.side3
    def getPerimeter(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def getSides(self):
        return [self.side1, self.side2, self.side3]
    def setSides(self, side1, side2, side3):
        self.side1 = 1
        self.side2 = 2
        self.side3 = 3
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return math.pi * (self.radius ** 2)
    def getPerimeter(self):
        return math.tau * self.radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius