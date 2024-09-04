class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):   # These classes
    def run(self):
        print(f"This rabbit is running")

class Fish(Animal):     # inherit characteristics
    def swim(self):
        print(f"This fish is swimming")

class Hawk(Animal):     # from the Animal class
    def fly(self):
        print(f"This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()



