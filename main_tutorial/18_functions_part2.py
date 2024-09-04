# *args =   parameter that will pack all the arguments into a tuple
#       =   useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args: # tuples are iterable
        sum += i
    return sum

print(add(1,2,3,4,5,6)) # sum is 21

# tuples are iterable, but they are ordered and unchangeable

def summing(*nums):
    sum = 0
    # nums[0] = 0 # this will not work because tuples do not support item assignments
    nums = list(nums) # typecast arguments into a list
                      # lists are mutable and changeable
    nums[0] = 0
    for i in nums:
        sum += i
    return sum

print(summing(1,2,3,4,5,6)) # first item on the list is changed to 0, so the sum is 20

# **kwargs = parameter that will pack all arguments into a dictionary
#          = useful so that a function can accept a varying amount of keyword arguments

# def hello(first,last):
#     print(f"Hello {first} {last}")

# hello(first = "Marot", middle = "Real", last = "Perisi") # multiple arguments; throws an error

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last']) # code now works, but does not display 3rd parameter
    print("\nHello ", end="")
    for key,value in kwargs.items(): print(value, end=" ") # prints the library for every key provided

hello(first = "Marot",middle = "Real",last = "Perisi")
hello(one = 'Haley', two = 'Kingdom')
