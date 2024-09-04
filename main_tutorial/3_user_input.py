# store inputs with the input() method

# name = input("Who are you? ") # stores the name as a string
# age = int(input("What is your age now? ")) # converts the string into an integer
# print(f"Your name is {name}. You are currently {age} years old. In 5 years, you will be {age+5} years old. Ew.")

def questions():
    name = input("Who are you? ")
    age = input("What is your age now? ")
    while not age.isdigit():
        print("Please enter a number.")
        age = input("What is your age now? ") # asks for age again, while keeping previous name.
    else:
        age = int(age) # reassign age as age converted to int()
        print(f"Your name is {name}. You are currently {age} years old. In 5 years, you will be {age+5} years old. Ew.")
    
questions()

