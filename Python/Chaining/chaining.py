
class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:",self.age)
        print("Is rewards member?", self.is_rewards_member)
        print("Gold card points:", self.gold_card_points)
        return self

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

user1 = User("Bob","Harrison","bob@gmail.com",39)
user2 = User("Susie","Thornton","email@email.com",60)
user3 = User("Zeb","Wells","zeb@hotmail.com",15)
user1.enroll().spend_points(50).enroll().display_info()
user2.enroll().spend_points(80).display_info()
user3.spend_points(40).display_info()