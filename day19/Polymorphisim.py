class Pet:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def speak(self):
        return "Some generic Sounds"

    def __gt__(self, other):
        return self.energy > other.energy

    def __add__(self, other):
        return PetGroup([self, other])


class Dog(Pet):
    def speak(self):
        return f"{self.name} barks: wolf wolf"


class Cat(Pet):
    def speak(self):
        return f"{self.name} mewo mewo"


class Duck(Pet):
    def speak(self):
        return f"{self.name} quack quack"


def perform_show(pet_list):
    print("Pet show is starting")
    for performer in pet_list:
        print(f"{performer.speak()}")
        print(f"{performer.play()}")


def makeAllSpeak(animalList):
    print("\n🎤 Let's hear from our pets:")
    for animal in animalList:
        print(f"{animal.speak()}")


class PetGroup:
    def __init__(self, pets):
        self.pets = pets

    def addPets(self, petOrPets):
        if isinstance(petOrPets, list):
            self.pets.extend(petOrPets)
            print(f"Added {len(petOrPets)} pets to the group")

        else:
            self.pets.append(petOrPets)
            print(f"Added {petOrPets.name} pet to the group")

    def __str__(self):
        names = [pet.name for pet in self.pets]
        return f"Pets Group : {','.join(names)}"


# =============create our pets ==================
dog = Dog("Buddy", energy=80)
cat = Cat("tommay", energy=60)
duck = Duck("daffy", energy=50)
robot = Duck("roboDuck", energy=90)


dog.speak()
cat.speak()
duck.speak()


makeAllSpeak([dog, cat, duck, robot])

print(f"Is Buddy more energetic than tommay?", "YES" if dog > cat else "NO")

group = dog + cat
print(f"Create a group with dog and cat : {group}")

group.addPets(duck)
group.addPets([Pet("Goldfish", 90), Pet("turtle", 50)])

print(f"Final group is {group}")
