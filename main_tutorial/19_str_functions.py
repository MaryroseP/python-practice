# 2.26.33
# str.format() =    optional method that gives users more control when
#                   displaying output

animal = "cow"
item = "moon"

# # print(f"The {animal} jumped over the {item}") # standard print statement
# print("The {} jumped over the {}".format("cow","moon")) # using values
# print("The {} jumped over the {}".format(animal,item)) # variables
# print("The {1} jumped over the {0}".format(animal,item)) # positional argyment
# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) # keyword arguments

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# adding padding
name = "Sia"
# print("Hello, my name is {:10}. Nice to meet you.".format(name))
# print("Hello, my name is {:<10}. Nice to meet you.".format(name)) # left align
# print("Hello, my name is {:>10}. Nice to meet you.".format(name))  # right align
# print("Hello, my name is {:^10}. Nice to meet you.".format(name)) # center align

number = 3.14159

print("The number pi is {:.2f}".format(number)) # f = for floating point numbers

money = 14051

print("This number is formatted with a comma: {:,}".format(money))
print("This is the binary equivalent of 14,051: {:b}".format(money))
print("This is the octal equivalent of 14,051: {:o}".format(money))
print("This is the hexadecimal equivalent of 14,051: {:X}".format(money))
print("This is the scientific notation equivalent of 10,000: {:e}".format(10000))













