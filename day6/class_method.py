class MyClass:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def person(self):
        print(
            f"My name is {self.name} i'm {self.age} years old. I live in {self.country} at {self.city} City"
        )


p1 = MyClass("irfan", 24, "Nanjing", "China")
p1.person()
# print(p1.age)
# print(p1.city)
# print(p1.country)


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} getting start")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} getting Off")


my_phone = Mobile("Samsung", "S6", 12000)
friend_phone = Mobile("iphone", "15pro max", 15000)

print(
    f"My phone is {my_phone.brand} my phone model is {my_phone.model} and price is {my_phone.price}"
)
my_phone.turn_on()
