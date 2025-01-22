import math

class Shape:
    def area(self):
        raise NoImplementedError("Subclass must implement abstract method 'area'")

#Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        return math.pi * (self.radius ** 2)

#Usage:
if __name__ == "__main__"
    #Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    #Display their areas
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Circle: {circle.area()}")