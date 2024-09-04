# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print(f"This duck is walking")

    def talk(self):
        print(f"This duck is quacking")

class Chicken:
    def walk(self):
        print(f"The chicken is walking")
    
    def talk(self):
        print(f"This chicken is clucking")

class Person():

    def catch(self,something):
        something.walk()
        something.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

