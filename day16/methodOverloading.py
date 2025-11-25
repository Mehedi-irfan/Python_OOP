class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def transaction(self, amount=None, to_account=None, description=""):
        if amount is None:
            return f"Current balance {self.balance}"
        elif to_account is None:
            self.balance += amount
            action = "Deposited" if amount > 0 else "Withdraw"
            return f"${abs(amount)} {action}. New balance is {self.balance}"
        else:
            if amount <= self.balance:
                self.balance -= amount
                return f"Transferred ${amount} to {to_account} for {description}. New Balance ${self.balance}"
            else:
                return "Insufficient Balance"


account = BankAccount(1000)

print(account.transaction())
print(account.transaction(500))
print(account.transaction(500, "Irfan"))
print(account.transaction(-500))
print(account.transaction(200, "Alvi", "Dinner"))
