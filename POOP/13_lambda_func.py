# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (thinks of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# lambda parameters:expression

# def double(x):
#     return x * 2

# print(double(5))

double = lambda x: x * 2
print(double(5))

multiply = lambda x,y: x * y
print(multiply(2,3))

add = lambda x,y,z: x + y + z
print(add(2,3,4))

full_name = lambda first_name, last_name : first_name+" "+last_name
print(full_name("Marot","Carrot"))

age_check= lambda age:True if age >= 18 else False
print(age_check(18))
