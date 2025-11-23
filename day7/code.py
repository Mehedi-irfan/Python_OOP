class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
print(calc.add(5, 8))
print(calc.multiply(5, 8))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"His name is {self.name} and his age is {self.age}")


p1 = Person("Arif", 25)
p1.get_info()


class BirthDayBoy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday you age is now {self.age}")


sakib = BirthDayBoy("sakib", 22)
sakib.celebrate_birthday()
sakib.celebrate_birthday()
sakib.celebrate_birthday()
