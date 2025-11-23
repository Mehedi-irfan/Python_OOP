class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
        self.heath = 100

    def eat(self):
        return f"{self.name} is eating!"

    def sleep(self):
        return f"{self.name} is sleeping!"

    def breath(self):
        return f"{self.name} is breathing"

    def get_heath(self):
        return f"{self.name} heath is {self.heath}%"


class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name, "Dog")
        self.bread = bread
        self.loyal = True

    def bark(self):
        return f"{self.name} is barking"

    def fetch(self):
        return f"{self.name} is fetching"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
        self.lives = 9

    def meow(self):
        return f"{self.name} is meowing: Meow! Meow! 🐈"

    def climb_tree(self):
        return f"{self.name} is climbing a tree 🌳"


# Object তৈরি
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "White")

print("=== DOG METHODS ===")
print(dog.eat())  # ✅ Inherited from Animal
print(dog.sleep())  # ✅ Inherited from Animal
print(dog.breath())  # ✅ Inherited from Animal
print(dog.bark())  # ✅ Dog-specific method
print(dog.fetch())  # ✅ Dog-specific method
print(dog.get_heath())  # ✅ Dog-specific method

print("\n=== CAT METHODS ===")
print(cat.eat())  # ✅ Inherited from Animal
print(cat.sleep())  # ✅ Inherited from Animal
print(cat.meow())  # ✅ Cat-specific method
print(cat.climb_tree())  # ✅ Cat-specific method
print(cat.get_heath())  # ✅ Cat-specific method

print("\n=== ATTRIBUTES ===")
print(f"Dog: {dog.name}, Breed: {dog.bread}, Loyal: {dog.loyal}")
print(f"Cat: {cat.name}, Color: {cat.color}, Lives: {cat.lives}")
