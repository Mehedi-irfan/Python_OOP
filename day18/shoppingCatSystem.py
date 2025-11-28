class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    # calculate the total price
    def __mul__(self, quantity):
        return self.price * quantity

    # combine same product
    def __add__(self, other):
        if self.name == other.name:
            return Product(self.name, self.price, self.quantity + other.quantity)
        else:
            return ValueError("Can only same product")

    # compare the product
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    # string representation
    def __str__(self):
        return f"{self.name} ({self.price} * {self.quantity})"


class ShoppingCart:
    def __init__(self):
        self.products = []

    # add product to the cart
    def __iadd__(self, product):
        for i, existingProduct in enumerate(self.products):
            if existingProduct == product:
                self.products[i].quantity += product.quantity
                break
        else:
            self.products.append(product)
        return self

    # marge two carts
    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.products = self.products.copy()

        for product in other.products:
            new_cart += product

        return new_cart

    # number of unique product
    def __len__(self):
        return len(self.products)

    # cart contents
    def __str__(self):
        if not self.products:
            return "cart is empty"

        items = "\n".join(f" - {product}" for product in self.products)
        total = sum(product.price * product.quantity for product in self.products)
        return f"Shopping cart : \n {items}\nTotal : ${total:.2f}"


laptop = Product("Laptop", 1000)
mouse = Product("mouse", 50)
keyboard = Product("keyboard", 70)

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1 += keyboard
cart1 += mouse
cart1 += laptop

cart2 += keyboard
cart2 += mouse
cart2 += laptop

print(cart1)
print(f"Unique product in cart1 : {len(cart1)}")


print(cart2)
print(f"Unique product in cart2 : {len(cart2)}")


merged_cart = cart1 + cart2
print("\nMerged Cart:")
print(merged_cart)
print(f"Unique products in merged cart: {len(merged_cart)}")

# Product operations
print(f"\nProduct Operations:")
print(f"2 Laptops cost: ${laptop * 2}")
print(f"Laptop == Mouse: {laptop == mouse}")

