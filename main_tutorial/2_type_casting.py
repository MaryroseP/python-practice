# type casting = convert data type to another data type (str -> int, etc)

x = 4 # integer (int)
y = 2.3 # float
z = "7" # string (str)

print(x)
print(y)
print(z)

print(x+y) # returns 6.3 because floats and integers can be used mathematically
# print(x+z) this throws an error because z is not an integer or a float and cannot be used mathematically

# instead, we have to convert it into an integer or a float using their respective methods:
#   int(<insert variable here>)
#   float(<insert variable here>)

print(x+int(z))     # this returns 11 since z = "7" was converted to an integer temporarily.

print(z*3)          # this will return 777 since z is still a string.

a = "4"             # a is a string
a = int(a)          # converting it to integer

print(a*3) # this returns 12 since a was converted and reassigned into an integer

# Where can this be used? ->> to concatenate integers to strings

# print("X is "+ x )      <-- This throws an error since you cannot concatenate strings with integers
print("X is "+ str(x))   # this returns "X is 4" since x was converted into a string.

# There is a method to bypass this however. This is by using the f-strings (formatted string literals). You can embed arithmetic operations
# and function calls as well

name = "Sandra"
age = 21

print(f"My name is {name} and I am {age} years old.")

