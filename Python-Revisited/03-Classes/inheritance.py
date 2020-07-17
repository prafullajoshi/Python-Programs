class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal : Parent, Base
# Mammal : Child, Sub


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal Constructor")
#         self.weight = 2

#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# m = Mammal()
# m.eat()
# print(m.age)

# MULTIPLE INHERITANCE


class Employee:
    def greet(self):
        print("Employee greeting")


class Person:
    def greet(self):
        print("Person greeting")


class Manager(Person, Employee):
    pass


m = Manager()
m.greet()  # greet() of Person will be invoked since we have written Employee class first in inheritance list
# Multiple inheritance is great choice if we know how to use it properly because if two base classes have something in common then it'll create ambuiguity and problems

# Look at following better example for multiple inheritance


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
