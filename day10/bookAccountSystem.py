# একটি "Car" class তৈরি করুন যার:
# ১. constructor এ brand, model, price attributes থাকবে
# ২. start_engine() method থাকবে - "Car engine started" return করবে
# ৩. car_info() method থাকবে - brand, model, price দেখাবে


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def start_engine(self):
        return f"{self.brand} car engine started"

    def car_info(self):
        return f"My car brand is {self.brand} and model is {self.model} and i bought it {self.price}$"


car = Car("Xiaomi", "SU7", 20000)
car1 = Car("Tesla", "Model X", 50000)
print(car.start_engine())
print(car1.start_engine())
print(car.car_info())
print(car1.car_info())


# Animal class তৈরি করুন এবং Dog, Cat child classes তৈরি করুন
# Animal class এ speak() method থাকবে
# Dog class এ speak() method override করে "Woof!" return করবে
# Cat class এ speak() method override করে "Meow!" return করবে


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        return f"{self.name} is Shouting"

    def animalInfo(self):
        return f"I have {self.name} his color is {self.color}"


class Dog(Animal):
    def __init__(
        self,
        name,
        color,
    ):
        super().__init__(name, color)

    def speak(self):
        return f"{self.name} speak Wolf"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def speak(self):
        return f"{self.name} speak Meow"


dog = Dog("bulldog", "Brown")
cat = Cat("Puppy", "white")
print(dog.speak())
print(cat.speak())
print(dog.animalInfo())
print(cat.animalInfo())

# Calculator class তৈরি করুন:
# ১. Class variable: calculator_type = "Scientific"
# ২. Class method: get_calculator_type() - calculator_type return করবে
# ৩. Static methods:
#    - add(a, b): দুটি number add করবে
#    - multiply(a, b): দুটি number multiply করবে
# ৪. Instance method: calculate_square(x): number এর square calculate করবে


class Calculator:
    Calculator_type = "Scientific"

    @classmethod
    def get_calculator_type(cls):
        return f"Calculator type is {cls}"

    @staticmethod
    def add(a, b):
        return f"Addition {a + b}"

    @staticmethod
    def multiply(a, b):
        return f"Multiply {a * b}"

    def calculate_square(self, x):
        return f"Square is {x} is {x**x}"


print(Calculator.get_calculator_type())
print(Calculator.add(50, 52))
print(Calculator.multiply(50, 52))
cal = Calculator()
print(cal.calculate_square(5))
