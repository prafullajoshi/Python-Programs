# Class : blueprint for creating class
# Object : Instance of class

# Class : Human
# Object : John, Marry, Jack

# CREARING CUSTOM CLASS
# class Point:
#     def draw(self):
#         print("draw")

# point = Point()
# point.draw()
# print(type(point))
# print(isinstance(point, Point))


# USE OF CONSTRUCTOR
# With self, we can refer to current object, we can access attributes of current object
# class Point:
#     default_color = "Red"       # Class attribute : Common for all instances of class

#     def __init__(self, x, y):
#         # super().__init__()
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point({self.x, self.y})")


# Point.default_color = "Yellow"
# point = Point(2, 5)
# print(point.default_color)
# print(Point.default_color)
# point.draw()

# another = Point(10, 29)
# print(another.default_color)
# another.draw()
# Here point and another are different objects and they are instance attributes


# CLASS METHOD : Factory Method
# class Point:
#     default_color = "Green"

#     def __init__(self, x, y):
#         # super().__init__()
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x, self.y})")


# point = Point.zero()
# point.draw()

# MAGIC METHODS : Factory Method; you define them to add magic to your class; always surrounded by double underscore
# class Point:
#     def __init__(self, x, y):
#         # super().__init__()
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x, self.y})")


# point = Point(2, 8)
# print(str(point))

# Comparing the objects


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 22)
other = Point(1, 20)
# references are compared, these two instances are pointing to diff references in memory therefore it prints False
print(point == other)
# To solve this issue, magic method __eq__() is used (https://rszalski.github.io/magicmethods/#comparisons)

# This will give TypeError; to solve this, we should define magic method __gt__(), then it will return proper result
print(point > other)

# This will give TypeError; to solve this, we should define magic method __add__(), then it will return proper result
print(point + other)
