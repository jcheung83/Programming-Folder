import parent

person1 = parent.Ninja("Tracy","Morgan",50,100,"Kane","Dog")
person2 = parent.Ninja("Bruce","Wayne",100,50,"Bobo","Hamster")
person3 = parent.Ninja("Stacy","Abrams",20,30,"Smalls","Snake")
person4 = parent.Ninja("Lilly","Hammer",100,100,"Peony","Cat")

person1.bathe().feed().walk().walk().feed().walk()
person2.bathe().feed().walk().bathe()
parent.Pet.print_pets()
parent.Ninja.print_ninjas()