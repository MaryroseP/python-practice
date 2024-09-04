# list comprehension =  a way to create new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [(expression) for (item) in (iterable)]
#       from example =  squares =[( i * i ) for ( i ) in ( range(1,11) )]



# First description
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i*i)     # define what each loop iteration should do 

print(squares)

squares = [i*i for i in range(1,11)]
print()



# Second description

students = [100,93,90,91,75,80,88,89,70,76,49,0]
# passed_students = list(filter(lambda x: x>60, students))
# print(passed_students)

# list comprehension format --> list = [(expression) for (item) in (iterable) if (conditional) ]
# passed_students = [i for i in students if i>=60]
# print(passed_students)

# list comprehension format --> list = [(expression) (if/else) for (item) in (iterable) ]
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)



