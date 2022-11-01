class BankAccount:
    
    bank_name = "Dojo First National"
    all_accounts = []
    
    def __init__(self, int_rate, balance): 
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
            print(f"${amount} was withdrawn. Your new balance is ${self.balance}.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        print(f"Interest rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance = self.balance * (self.int_rate/100 + 1)
        self.balance = "{:.2f}".format(self.balance)
        print(f"After yielding interest at {self.int_rate}%, your new balance is ${self.balance}.")
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}, interest rate: {account.int_rate}%.")

class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.checking_account = BankAccount(int_rate=0.001,balance=0)
        self.savings_account = BankAccount(int_rate=0.05,balance=0)
        self.account = [None]*10000

    def display_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:",self.age)
        print("Is rewards member?", self.is_rewards_member)
        print("Gold card points:", self.gold_card_points)

    def enroll(self):
        if (self.is_rewards_member == True):
            print(self.first_name + " is already a member, cannot enroll again")
        else:
            print(self.first_name + " is now a rewards member")
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if (amount<=self.gold_card_points):
            print(str(amount) + " points were deducted from " + self.first_name + "'s account")
            self.gold_card_points -= amount
        else:
            print(self.first_name + " does not have enough points, no points were deducted")
        return self

    def make_deposit(self, type, amount):
        if (type == "checking account"):
            self.checking_account.balance += amount
            print(f"${amount} was deposited in your {type}. Your new balance is ${self.checking_account.balance}.")
        elif (type == "savings account"):
            self.savings_account.balance += amount
            print(f"${amount} was deposited in your {type}. Your new balance is ${self.savings_account.balance}.")
        return self

    def withdraw(self, type, amount):
        if (type == "checking account"):
            if amount > self.checking_account.balance:
                print("Insufficient funds! Charging a $5 fee")
                self.checking_account.balance -= 5
            else:
                self.checking_account.balance -= amount
                print(f"${amount} was withdrawn. Your new balance is ${self.checking_account.balance}.")
        elif (type == "savings account"):
            if amount > self.savings_account.balance:
                print("Insufficient funds! Charging a $5 fee")
                self.savings_account.balance -= 5
            else:
                self.savings_account.balance -= amount
                print(f"${amount} was withdrawn. Your new balance is ${self.savings_account.balance}.")
        return self

    def display_user_balance(self):
        print(f"Current checking account balance: ${self.checking_account.balance}")
        print(f"Current savings account balance: ${self.savings_account.balance}")

    def transfer_money(self, amount, type, other_user):
        if (type == "checking account"):
            if amount > self.checking_account.balance:
                print("Insufficient funds! Transfer cancelled.")
            else:
                self.checking_account.balance -= amount
                other_user.checking_account.balance += amount
                print(f"${amount} was transferred from {self.first_name}'s checking account to {other_user.first_name}'s checking account.")
        if (type == "savings account"):
            if amount > self.savings_account.balance:
                print("Insufficient funds! Transfer cancelled.")
            else:
                self.savings_account.balance -= amount
                other_user.checking_account.balance += amount
                print(f"${amount} was transferred from {self.first_name}'s savings account to {other_user.first_name}'s checking account.")
        return self

    def create_account(self):
        number = input("What number is associated with this new account (limit is 4 digits)? ")
        number = int(number)
        if self.account[number] != None:
            print("This account already exists, cancelling account creation.")
        else:
            print(f"Depositing $1 into account {number} as a thank you gift.")
            self.account[number] = BankAccount(int_rate=.001,balance=1)
        return self

user1 = User("Bob","Jones","email",20)
user2 = User("Billy","Sylvestor","email",80)
user1.create_account().create_account().create_account()

user1.make_deposit("checking account",800).make_deposit("savings account",200).withdraw("savings account",250).withdraw("checking account",100).transfer_money(50, "checking account", user2).display_user_balance()
user2.display_user_balance()