class Product:
    company = "TechShop"

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = True

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount
        return f"discount applied. new price is ${self.price}"

    @classmethod
    def get_company_info(cls):
        return f"Welcome to {cls.company}"

    @staticmethod
    def is_valid(price):
        return price > 0

    def product_info(self):
        return f"{self.name} - ${self.price} {self.category}"


class ElectronicsProduct(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price, "Electronics")
        self.brand = brand
        self.warranty = warranty

    def product_info(self):
        base_info = super().product_info()
        return f"{base_info} - Brand {self.brand} Warranty {self.warranty} Years"


laptop = ElectronicsProduct("Gaming Laptop", 584600, "Asus", 10)
print(laptop.product_info())
print(laptop.apply_discount(10))
print(laptop.get_company_info())
print(f"Valid Price :- {Product.is_valid(1000 )}")
