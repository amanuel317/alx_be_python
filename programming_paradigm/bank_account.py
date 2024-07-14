# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return self.account_balance
        else:
            print("Insufficient funds.")
            return None
    def get_balance(self):
        return f"Current Balance: {self.account_balance}"

    def display_balance(self):
        return self.account_balance
