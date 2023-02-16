from faker import Faker
import random

class Account:
    def __init__(self, aid, name):
        self.id = aid
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self):
        pass

    def check_balance(self):
        return self.balance


class Checking(Account):
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Not enough balance")
        else:
            print("Withdraw amount must be positive")


class Savings(Account):
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance and amount < 200:
                self.balance -= amount
            else:
                print("Not enough balance")
        else:
            print("Withdraw amount must be positive")


class Bank:
    def __init__(self):
        self.accounts = []

    def load_accounts(self):
        for i in range(20, 41):
            t = random.randint(0, 1)
            if t == 0:
                bank.accounts.append(Checking(i, faker.first_name() + " " + faker.last_name()))
            else:
                bank.accounts.append(Savings(i, faker.first_name() + " " + faker.last_name()))

    def print_accounts(self):
        for ac in bank.accounts:
            print(ac.id, ac.name)

    def get_account(self, aid):
        for ac in self.accounts:
            if ac.id == aid:
                return ac
        return None



faker = Faker()
bank = Bank()
bank.load_accounts()
# bank.print_accounts()

while True:
    print()
    aid = int(input("Give ID: (0 to exit) "))
    if aid == 0:
        break
    account = bank.get_account(aid)
    if account is None:
        print("Account does not exist")
        continue
    # How we can also print the account type in the welcome message
    print("Welcome", account.name)
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("0. EXIT")
        choice = int(input("Choose: "))
        if choice == 1:
            # ask for amount
            # deposit the amount
            pass
        elif choice == 2:
            # ask for amount
            # withdraw the amount
            pass
        elif choice == 3:
            # display the balance
            pass
        elif choice == 0:
            break
        else:
            print("Invalid choice")






