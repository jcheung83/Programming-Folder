class BankAccount:
    
    bank_name = "Dojo First National"
    all_accounts = []
    
    def __init__(self, name, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} was deposited. Your new balance is ${self.balance:.2f}.")
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            print(f"${amount} was withdrawn. Your new balance is ${self.balance:.2f}.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        print(f"Interest rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance = self.balance * (self.int_rate/100 + 1)
        # self.balance = "{:,.2f}".format(self.balance)
        print(f"After yielding interest at {self.int_rate}%, your new balance is ${self.balance:.2f}.")
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print(f"Name: {account.name}, balance: ${account.balance:.2f}, interest rate: {account.int_rate}%.")

account1 = BankAccount("Jerry",1.00, 5000)
account2 = BankAccount("Hannah",1.50, 25000)
account1.deposit(2000).deposit(58000).withdraw(65000).withdraw(5).display_account_info()
account2.deposit(80000).deposit(25000).withdraw(50000).withdraw(10000).withdraw(21000).withdraw(30000).yield_interest().display_account_info()

BankAccount.all_balances()