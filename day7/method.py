class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} his age is {self.age}"


p1 = Person("korim", 91)
print(p1)
