# exception = events detected during execution that interrupts the flow of a program

# numerator = int(input("Enter a number to divide: "))
# denominator = int(input("Enter a number to divide by: "))
# result = numerator/denominator
# print(result)

# when the user inputs 0 into the denominator it throws an error, which is tje ZeroDivisionError
# another way of writing this code:

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Can only input numbers")
# except Exception:
#     print("Something went wrong :C") # this catches ALL exceptions, however it is not the best practice
else: print(result)
finally:
    # this block of code will always execute after this
    print("Skibidi Toilet")

# explanation for the code:

# the block of code in 'try' will execute first, and exeptions caught are reported. if there are no exceptions,
# the result will be printed in the else block. At the last part is finally, and this is a block of code that
# will always execute