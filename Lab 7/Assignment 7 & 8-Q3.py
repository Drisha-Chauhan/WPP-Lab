class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, balance):
        self.accounts[acc_no] = balance

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no] += amount

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts and self.accounts[acc_no] >= amount:
            self.accounts[acc_no] -= amount

    def display_accounts(self):
        for acc_no, balance in self.accounts.items():
            print(f"Account {acc_no}: Balance {balance}")

bank = Bank()

bank.create_account(input("Enter account number: "), int(input("Enter initial balance: ")))

bank.deposit(input("Enter account number: "), int(input("Enter deposit amount: ")))

bank.withdraw(input("Enter account number: "), int(input("Enter withdrawal amount: ")))

bank.display_accounts()
