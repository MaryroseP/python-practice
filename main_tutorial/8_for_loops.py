import time

# for loops =   a statememnt that will execute its block of code a limited amount of times

#               while loop  = unlimited repetition
#               for loop    = limited repetition (for n times)


# for i in range(10):
#    print(i)                # prints index (0-9). So it basically counts from 0-9 since computer index starts at 0
#    print(i+1)              # prints 0-10
#    print("Hello World!")   # prints "Hello World!" 10 times
    
# for i in range(1,10): # starts at 1, ends at 10
#    print(i) # prints 1-10

# for i in range (2,20+2,2): # starts at 2, ends at 20+2 (increment), by 2 steps
#    print(i) # prints 2-20 by 2s

# for i in "Maroot":
#    print(i)

for seconds in range(10,0,-1): # starts at 10, ends at 0, counting -1 step (backwards)
    print(seconds)
    time.sleep(1)
print("Time's up!")