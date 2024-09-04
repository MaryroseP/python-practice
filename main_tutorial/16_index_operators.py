# index operators [] =  gives access to a sequence's element (str, list, tuples)

name = "mary Rose"

# if (name[0].islower()):
#     name = name.capitalize()

first_name = name[:4].upper()
last_name = name[5:].lower()

print(first_name)
print(last_name)