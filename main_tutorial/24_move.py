import os
# let's first write a file

# text = "Hello"
# with open('testing.txt','w') as file:
#     file.write(text)

source = "testing.txt"
destination = "C:\\Users\\Marot\\Desktop\\testing.txt"

try:
    if os.path.exists(destination):
        print("The is already a file there")
    else:
        os.replace(source,destination)
        print(f"{source} was moved")
except FileExistsError:
    print(f"{source} does not exist")
