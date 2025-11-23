# ১. "Laptop" ক্লাস তৈরি করুন যার attributes হবে:
#    - brand, model, processor, ram, price


class Laptop:
    def __init__(self, brand, model, processor, ram, price):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.price = price

    def is_laptop(self):
        print(
            f"My Laptop is {self.brand} model is {self.model} processor is {self.processor} and ram is {self.ram} price is {self.price}"
        )


my_Laptop = Laptop("Dell", "Inspirion", "Corei i3", "8GB", "44k")
friend_Laptop = Laptop("HP", "probook", "Corei i5", "16GB", "87k")


my_Laptop.is_laptop()
friend_Laptop.is_laptop()

# ২. "BankAccount" ক্লাস তৈরি করুন:
#    - account_holder, account_number, balance


class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.is_account_open = False

    def open_account(self):
        self.is_account_open = True
        print(f"{self.account_holder} account is OPEN")

    def close_account(self):
        self.is_account_open = False
        print(f"{self.account_holder} account is CLOSE")

    def account_info(self):
        status = "OPEN" if self.is_account_open else "CLOSE"
        print("🏦 Account Information:")
        print(f"   Holder: {self.account_holder}")
        print(f"   Account No: {self.account_number}")
        print(f"   Balance: {self.balance} Taka")
        print(f"   Status: {status}")
        print("-" * 30)


my_account = BankAccount("Irfan", "214675435", "50,00,000")
rahim_account = BankAccount("Rahim", "4579241", "1,04,52,640")

my_account.open_account()
my_account.account_info()

rahim_account.close_account()
rahim_account.account_info()


#
