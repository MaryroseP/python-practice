import os

path = "C:\\Users\\Marot\\Documents\\Python Practice\\python course\\trial\\test.txt"

if os.path.exists(path):
    print("Exists")
    if os.path.isfile(path):
        print("A file")
    elif os.path.isdir(path):
        print("A directory")
else:
    print("Does not exist")

print("\n")

with open("C:\\Users\\Marot\\Documents\\Python Practice\\python course\\trial\\test.txt") as file: # can also use the file name but make sure that the program is in the same directory
    print(file.read()) # file is printed out into the console
print(file.closed)

# ^ This block of code does not handle exceptions

try:
    with open('randomfile.py') as file: # can also use the file name but make sure that the program is in the same directory
        print(file.read()) # file is printed out into the console
        print(file.closed)
except FileNotFoundError:
    print("No file found")


# text = "Eyoooooo\nYou like this text?\nI made it"
# with open('try.txt','w') as file:
#     file.write(text)

text = "I added contents to the file"
with open('try.txt','a') as file: # append
    file.write(text)
