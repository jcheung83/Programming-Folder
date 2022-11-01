class Ninja:
    allNinjas=[]

    def __init__(self, first_name, last_name, treats, pet_food, pet, animal_type):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        if(animal_type == "Dog"):
            self.pet = Dog(name=pet, type="Dog", tricks="fetch; roll over; sit")
        elif(animal_type == "Cat"):
            self.pet = Cat(name=pet, type="Cat", tricks="none")
        elif(animal_type == "Bird"):
            self.pet = Bird(name=pet, type="Bird", tricks="speak")
        elif(animal_type == "Snake"):
            self.pet = Snake(name=pet, type="Snake", tricks="eat mice")
        else:
            self.pet = Pet(name=pet, type=animal_type, tricks="none")
        Ninja.allNinjas.append(self)
        
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"Taking {self.pet.name} the {self.pet.type} for a walk!")
        return self
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        if self.pet_food <= 0:
            print(f"Oh no, we're out of food! {self.pet.name} is going to be hungry until you get more!")
        else:
            print(f"Feeding {self.pet.name}! Yum!")
            self.pet_food -= 5
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"Bathing {self.pet.name} the {self.pet.type}, who makes this sound:")
        self.pet.noise()
        return self
    
    @classmethod
    def print_ninjas(cls):
        for ninjas in cls.allNinjas:
            print(f"Name: {ninjas.first_name} {ninjas.last_name}, treats: {ninjas.treats}, pet food: {ninjas.pet_food}, pet: {ninjas.pet.name}, type: {ninjas.pet.type}, tricks: {ninjas.pet.tricks}, energy: {ninjas.pet.energy}, health: {ninjas.pet.health}")

class Pet:
    allpets=[]

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.energy = 100
        self.health = 100
        self.tricks = tricks
        Pet.allpets.append(self)

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print("relevant pet sound")
        return self

    @classmethod
    def print_pets(cls):
        for pets in cls.allpets:
            print(f"Name: {pets.name}, type: {pets.type}, tricks: {pets.tricks}, energy: {pets.energy}, health: {pets.health}")

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def noise(self):
        print("bark")
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def noise(self):
        print("meow")
        return self

class Bird(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def noise(self):
        print("chirp")
        return self

class Snake(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def noise(self):
        print("hsssss")
        return self