# There are multiple functions exist which are used to read , write , update or can do many other tasks 
# as well 
# now we will be looking towards the readlines() function
# actually it is also just reading the files so there is no need to tell the file to open it in the read mode
# because it is already in the read mode by default
f = open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/functions.txt")
lines = f.readlines()
print(lines , type(lines))
f.close()
# now there exist a differnce if we use the function readlines() it will print the all lines in the 
# form of the list and will display the list completely but if we use the function readline it will 
# display the content line by line in the form of strings 
f = open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/functions.txt")
line1 = f.readline()
print(line1 , type(line1))

line2 = f.readline()
print(line2 , type(line2))

line3 = f.readline()
print(line3 , type(line3))

line4 = f.readline()
print(line4 , type(line4))

line5 = f.readline()
print(line5 , type(line5))
f.close()


# this all work can also be done using the loop like we will be using the while loop
f = open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/functions.txt")
line = f.readline()
while(line!= ""):
    print(line)
    line = f.readline()
f.close()

# now we will be discussing the append mode as well 
str= "\nI am a student"
f = open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/functions.txt", "a")
f.write(str)
f.close()

# now the next thing to study is the use of with statement
# Actually it is very beneficial in the context of close() statement like if we use it we do not 
# have to use the close() statement again and again
str= "\nI am a student"
with open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/functions.txt", "a") as f:
    f.write(str)


# now we will be making the use of "+" operater with other modes like w,r,a as well
# str= "\nI am a student"
with open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/functions.txt", "r+") as f:
    result = f.read()
    print(result)
    f.write("we are updating the text like we are in the update mode")

    