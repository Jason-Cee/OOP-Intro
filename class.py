# OOP Intro
# Name Class
class Shapes:
    # Initialising my attributes

    def __init__(self, type, name, side, size):
        self.type = type
        self.name = name
        self.side = side
        self.size = size

    # Method
    def area(self):
        print("This is a: " + self.type + "\n" +
              "The name is: " + self.name + "\n" +
              "The amount of sides: " + self.side + "\n" +
              "The size is: " + self.size)


# Call
objShapes = Shapes("Shape", "Square", "4", "Area")
objShapes.area()


# Name Class
class Circle(Shapes):
    # Initialising my attributes
    def __init__(self, radius):
        self.radius = radius

    # Method
    def area(self):
        result = 3.14 * self.radius * self.radius
        return result

    # Call


objcoin = Circle(5)
print(objcoin.area())


# Name Class
class Triangle(Shapes):
    # Initialising my attributes
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # Method
    def area(self):
        area_Triangle = 0.5 * self.base * self.height
        return area_Triangle

    # Call


objpyramid = Triangle(7, 4)
print(objpyramid.area())


# Name Class
class Rectangle(Shapes):
    # Initialising my attributes
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # Method
    def area(self):
        area_Rectangle = self.width * self.height
        return area_Rectangle

    # Call


objlaptop = Rectangle(7, 4)
print(objlaptop.area())


# Name class
class Square(Shapes):
    # Initialising my attributes
    def __init__(self, side):
        self.side = side

    # Method
    def area(self):
        area_Square = self.side * 4
        return area_Square

    # Call


objcube = Square(5)
print(objcube.area())
