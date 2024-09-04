import os
import shutil as sht # for directories with files in them

# write a file first
# text = "This is random text"
# with open('wow.txt','w') as file:
#     file.write(text)

try:
    # os.remove('wow.txt') # delete individual files
    # os.rmdir('rand') # delete empty directory
    sht.rmtree('folder') # delete directory with files
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You have no permission to delete this file.")
except OSError:
    print("Cannot delete folder with files inside")
else:
    print("The file was deleted")