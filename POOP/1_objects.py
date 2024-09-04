# objects = instance of a class
# attributes = what an object is or has
# methods = what it can do
# class = functions as a blueprint that describes what attributes and methods
# a distinct class will have

# class Car: # naming convention: starts with a capital letter
#     pass

from Z_car_2A import Car

# Car.wheels = 6 # This affects all instances

car_1 = Car("Mistubishi", "Kakarot", 2003, "Blue")
car_1.drive()
car_1.wheels = 2
print(f"The {car_1.model} model has {car_1.wheels} wheels.")
print()

car_2 = Car("Toyota", "Motor", 2012, "Red")
car_2.stop()
print(f"The {car_2.model} model has {car_2.wheels} wheels.")
print()

print(f"The default number of wheels is {Car.wheels}.")