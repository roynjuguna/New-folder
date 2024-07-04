class Animal:
    def walk(self):
        print (" walking")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 10)

print(f"{roger.name} who is {roger.age} is {roger.walk()}")

roger.walk()