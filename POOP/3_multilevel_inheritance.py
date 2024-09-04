class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print(f"This animal is eating.")

    def sleep(self):
        print(f"This animal is asleep.")

    
class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking")

dog1 = Dog("Charlie")

print(f"Is the dog alive?: {dog1.alive}")
dog1.eat()
dog1.sleep()
dog1.bark()