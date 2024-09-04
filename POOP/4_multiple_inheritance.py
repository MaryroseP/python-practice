# multiple inheritance = child class inherits from more than one parent class

class Prey:

    def flee(self):
        print(f"This animal flees")

class Predator():

    def hunt(self):
        print(f"This animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()