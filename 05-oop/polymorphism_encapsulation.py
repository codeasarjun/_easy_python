
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def set_dimensions(self, width, height):
        self.__width = width
        self.__height = height

    def get_dimensions(self):
        return (self.__width, self.__height)

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        import math
        return math.pi * (self.__radius ** 2)

rect = Rectangle(4, 5)
print(f"Rectangle area: {rect.area()}")

circ = Circle(3)
print(f"Circle area: {circ.area()}")
