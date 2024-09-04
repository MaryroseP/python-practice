# dictionary = a changeable, ordered collection of unique key:value pairs
#             fast because they use hashing, allows us to access value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

# capitals.update({'Germany':'Berlin'})
# print(capitals['Germany'])

# # To check if the item is in the dictionary, use get() method
# print(capitals.get('Philippines')) # This returns 'None'

# # Assortment of Methods for dictionaries:
# print(capitals.keys()) # prints only the keys and not the values
# print(capitals.values()) # prints all the values
# print(capitals.items()) # prints both
# capitals.pop('China') # removes china and its value
# capitals.clear() # Clears dictionary


# another way to print all the items in the dictionary.
for key,value in capitals.items():
    print(key,value)

