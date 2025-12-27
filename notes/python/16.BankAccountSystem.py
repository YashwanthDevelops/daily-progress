def validate_transaction(func):
    def wrapper(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return 
        return func(self, amount)
    return wrapper


class BankAccount:
    band_name = "Python Bank"
    interest_rate = 0.04

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        # self.account_number = account_number
    
    @validate_transaction
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    @validate_transaction
    def withdraw(self, amount):
        self.balance = self.balance - amount

    @classmethod
    def change_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        
    def __str__(self):
        return'{}, {}'.format(self.account_holder, self.balance)

    def __repr__(self):
        return 'BankAccount({}, {})'.format(self.account_holder, self.balance)

    def __add__(self, other):
        return self.balance + other.balance


class SavingsAccount(BankAccount):
    interest_rate = 0.06

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    withdraw_fee = 50
    def withdraw(self, amount):
        total = amount + self.withdraw_fee
        self.balance -= total

acc1 = SavingsAccount("Yash", 10000)
acc2 = CheckingAccount("Rahul", 5000)

acc1.deposit(2000)
acc1.apply_interest()

acc2.withdraw(1000)

print(acc1)
print(acc2)

total = acc1 + acc2
print("Total Balance:", total)
