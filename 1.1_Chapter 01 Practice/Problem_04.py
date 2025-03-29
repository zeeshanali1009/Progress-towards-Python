# python program to list the directories of the selected folder 
# Importing the os module in the ide
import os

# Setting the path which we want to show with details
directory_path = "/"

# listing
content = os.listdir(directory_path)

# printing
for item in content:
    print(item)