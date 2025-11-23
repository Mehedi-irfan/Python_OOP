class Vehicles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f" {self.brand} {self.model} engine started"

    def get_info(self):
        return f"Vehicles : {self.brand} {self.model}"


class Car(Vehicles):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def start_engine(self):
        parent_result = super().start_engine()
        return f"{parent_result} with {self.fuel_type} fuel"

    def get_info(self):
        return f"{self.brand} {self.model} with ({self.fuel_type})"


class ElectricCar(Vehicles):
    def __init__(self, brand, model, batteryCapacity):
        super().__init__(brand, model)
        self.batteryCapacity = batteryCapacity

    def start_engine(self):
        return f"{self.brand} {self.model} Silently Power On"

    def get_info(self):
        return f"Electric car {self.brand} {self.model} ({self.batteryCapacity}KWH)"


car = Car("Toyota", "Corolla", "petrol")
electricCar = ElectricCar("Tesla", "Model S", "100")

print(car.start_engine())
print(electricCar.start_engine())
print(car.get_info())
print(electricCar.get_info())
