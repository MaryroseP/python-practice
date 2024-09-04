class Car:

    color = None

class Motorcycle:

    color = None

def change_color(car,color):
    car.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()
bike = Motorcycle()

change_color(car_1,"Red")
change_color(car_2,"Blue")
change_color(car_3,"Yellow")
change_color(bike,"Black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike.color)


 