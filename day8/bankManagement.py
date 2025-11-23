class BankAccount:
    bank_name = "Bangladesh Bank"

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    @classmethod
    def bankInfo(cls):
        return f"Bank Name :- {cls.bank_name}"

    @staticmethod
    def is_account_valid(acc_number):
        return len(str(acc_number)) == 10

    # instance Method
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited Amount is {amount} after deposit your Total amount is {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdraw {amount} and New balance is {self.balance}"
        return "Insufficient Balance"


account = BankAccount("irfan", 7894561235, 1000)
print(account.bankInfo())
print(account.is_account_valid(7894561235))
print(account.deposit(500))
print(account.withdraw(200))


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0, interest_rate=2.5):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = 500

    def withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            return f"Withdraw Amount {amount}. New Balance {self.balance}"
        else:
            return f"Can't withdraw Minimum {self.minimum_balance} must remain "

    def addInterest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.interest_rate += interest
        return f"Your interest {interest:.2f} added. New Balance is  {self.balance:.2f}"

    def accountInfo(self):
        return f"Saving Acount : - Holder : {self.account_holder}, Balance is {self.balance} Interest Rate is {self.interest_rate}%"


class CurrentAcount(BankAccount):
    def __init__(
        self, account_holder, account_number, balance=0, overdraft_limit=10000
    ):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        max_withdraw = self.balance + self.overdraft_limit
        if amount <= max_withdraw:
            self.balance -= amount
            return f"withdraw {amount}. New Balance is {self.balance}"
        else:
            return f"Can't withdraw maximum Overdraft limit is {self.overdraft_limit}"

    def get_overdraft_info(self):
        return f"Current - account :- Overdraft Limit {self.overdraft_limit} and available Balance is {self.balance + self.overdraft_limit} "


print("========Savings Account==========")
saving_acc = SavingsAccount("Mehedi", 457896412, 3000, 3.0)
print(saving_acc.accountInfo())
print(saving_acc.deposit(500))
print(saving_acc.withdraw(1000))
print(saving_acc.withdraw(2000))
print(saving_acc.addInterest())
print(saving_acc.accountInfo())


print("\n" + "=" * 50 + "\n")

print("========Current Account==========")
current_acc = CurrentAcount("Rakib", 7486942, 4000, 15000)
print(current_acc.get_overdraft_info())
print(current_acc.deposit(2000))
print(current_acc.withdraw(3000))
print(current_acc.withdraw(10000))
print(current_acc.withdraw(20000))
print(current_acc.get_overdraft_info())

print("\n" + "=" * 50 + "\n")

# ✅ BankInfo and Validation Test
print("=== BANK INFO & VALIDATION ===")
print(SavingsAccount.bankInfo())
print(CurrentAcount.bankInfo())
print(f"Account valid: {BankAccount.is_account_valid('1234567890')}")
print(f"Account valid: {BankAccount.is_account_valid('12345')}")
