# random

import random as rnd

x = rnd.randint(1,6)
print(x)

y = rnd.random()
print(y)

myList = ['rock', 'paper', 'scissors']
z = rnd.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
rnd.shuffle(cards)
print(cards)