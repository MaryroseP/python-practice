# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude","Bro","Mister","admin"]
passwords = ("p@sswords","abc123","guest","admin")

# users = zip(usernames,passwords) # zip objects are iterable

# for i in users:
#     print(i)

# output
# ('Dude', 'p@sswords')
# ('Bro', 'abc123')  
# ('Mister', 'guest')
# ('admin', 'admin') 

users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(f"{key}: {value}")

number = ('999','1010','8008')

user = zip(usernames,passwords,number)
for i in user:
    print(i)
