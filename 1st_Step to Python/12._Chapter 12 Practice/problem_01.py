# This program opens the three existing files and if they do not exist print the value error



try:
    with open("file+01.txt") as f:
        print(f.read())
except Exception as e:
        print(e)
try:
    with open("file_02.txt") as f:
        print(f.read())
except Exception as e:
        print(e)
try:    
    with open("file_03.txt") as f:
        print(f.read())
except Exception as e:
        print(e)

print("Thank you!")
