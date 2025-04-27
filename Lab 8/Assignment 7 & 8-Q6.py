class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def display(self):
        print(f"Account {self.acc_no}: Balance {self.balance}")

account = BankAccount(input("Enter account number: "), int(input("Enter initial balance: ")))
account.deposit(int(input("Enter deposit amount: ")))
account.withdraw(int(input("Enter withdrawal amount: ")))
account.display()


