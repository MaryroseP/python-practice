# if statements = a block of code that will execute if its conditions is true


age = int(input("How old are you? "))
if age == 100: # if age is equal to 100
    print(f"Damn you're a century old.")
elif age >= 18: # if the age is greater than or equal to 18
    print(f"You are {age}, and you are of legal age.")
elif age < 0:
    print(f"It's impossible that you have not been born yet and can type out an answer.")
else: # if not greater than or equal to 18
    print(f"You are {age}, and are not of legal age.")


# logical operators (and, or, not) = checks if two or more conditional statements are true
    
temp = int(input("What's the temperature outside today?" ))

if temp >= 0 and temp <=30:
    print("Nice weather out. Get some air.")
elif temp < 0 or temp > 30:
    print("Nope, don't go outside.")





