string = "PortmanteaU"
word = "libertine"

print(len(string)) # returns the number of characters in the string
print(string.find("a")) # returns the first instance of the character you are trying to find (starting from 0)
print(word.capitalize()) # capitalizes the first letter of the first word
print(word.upper()) # turns all letters to uppercase
print(word.lower()) # turns all letters to lowercase
print(string.isdigit()) # returns a boolean. checks if the string is numerical
print(string.isalpha()) # returns a boolean. checks if the strings are alphabets
print(string.count("a")) # returns the number of instances a character appears
print(string.replace("a","o")) # replaces the first parameter with the second parameter