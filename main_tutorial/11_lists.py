# lists = stores multiple items in one variable

food = ["pizza", "ice cream", "carrot", "chicken"]

print(food)     # prints everything
print(food[0])  # prints first element

print("-----------")

# update lists

food[0] = "milk"    # first element is replaced by 'milk'
food.append("cream")
food.append("cake")
food.append("rice")

print("The following were appended: \n 'cream', 'cake', 'rice'")
print(food)

print("-----------")

print("Iterated over the list:")

for x in food:
    print(x)



print(food)

print("-----------")

food.remove("carrot") # removes a specific item in the list
print(food)
print("-----------")
food.pop() # removes the last item in the list
print(food)
print("-----------")
food.insert(0, "cheese") # inserts item at index n
print(food)
print("-----------")
food.sort() # sorts the items in order
print(food)
print("-----------")
food.clear()

