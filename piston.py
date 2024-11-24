#Parent (Base class) - класс, от которого наследуются
import math
class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Child(Parent):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)

    def introduce(self):
        print(f"Hello, im a child, my name is {self.name}")

    def greet(self):
        super().greet()
        print("Wsp lil bro ")

parent = Parent("Voblamobla")
child = Child("Jayson", 10)

parent.greet()
child.greet()

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def show_info(self):
        print(f"Name:{self.name}, position: {self.position}")

class Developer(Employee):
    def __init__(self,name,position,prog_lang = []):
        super().__init__(name,position)
        self.prog_lang = prog_lang

    def show_info(self):
        super().show_info()
        print(f"Programming languages: {self.prog_lang}")

iosDev = Developer("Nuradil", "Middle", ["swift", "UIKit", "SwiftUI", "Objective-C"])

iosDev.show_info()

class Shape:
    def area(self):
        return "Площадь отсутствует"

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

rectangle = Rectangle(2 ,4)
print(rectangle.area())

circle = Circle(5)
print(circle.area())

shape = Shape
print(shape)

class Character:
    def __init__(self, name, health, damage):
        self.name=name
        self.health=health
        self.damage=damage

    def attack(self):
        print(f"Персонаж {self.name} производит атаку и наносит противнику {self.damage} урона!")

    def take_damage(self):
        self.health -= self.damage
        print(f"HP Персонажа понизилось на {self.damage}")
        if self.health < 0:
            print("Персонаж погиб!")

class Soldier(Character):
    def __init__(self, name, health, damage, weapon):
        super().__init__(name,health,damage)
        self.weapon = weapon

    def attack(self):
        print(f"Персонаж {self.name} производит атаку с помощью {self.weapon} и наносит противнику {self.damage + 8} урона!")


class Sniper(Character):
    def __init__(self, name, health, damage, range):
        super().__init__(name, health, damage)
        self.range = range

    def attack(self):
        print(
            f"Персонаж {self.name} производит атаку с дистанции {self.range} метров, и наносит противнику {self.damage - 5} урона!")

char1 = Character("Dirlahan", 4, 3)
char1.attack()
char2 = Sniper("Dirlahan", 4, 6, 15)
char2.attack()

