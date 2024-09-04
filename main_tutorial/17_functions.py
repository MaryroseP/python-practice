# function = a block of code that executes only when called

def hello(name, surname,age): # Parameters
    print(f"Hello {name}! Your family name is {surname}\nYour age is {age} \nHave a nice day.")

hello("Maryrose", "Pergis", 21) # Arguments

# return statement = return the function's value back to the caller

def age_in_korea(age):
    k = age + 1
    return k

print(age_in_korea(20))

def multiplication(num1, num2):
    return num1 * num2

print(multiplication(2,4))


# keyword arguments = preceeded by an identifier, order does not matter

def candybars():
    three = input("Least favorite candy bar: ")
    two = input("How about the second one?: ")
    one = input("And the best? ")
    print(f"These are your favorite candy bars, starting from most liked:\n {one}, {two}, {three}")

# candybars()

def hello1(first,middle,last):
    print(f"Hello {first} {middle} {last}")

hello1(last="Pers", middle="hell", first="Yo")

# # nested function calls = function calls inside other function calls
#                           innermost functioncalls are resolved first
#                           returned value is used as argument for the next outer function

# Original code:

# num = input("Enter a whole positive number: ")
# num = float(num) # converts string into a float
# num = abs(num) # returns the absolute value of num
# num = round(num) # rounds the number
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))

# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created


def myColor():
    color = input("What color do you want?: ") # local variable - only exists inside the function
    print(color)                               # or set region

myColor()

color = "Red" # global variable - available inside and outside functions
print(color)









