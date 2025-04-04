# File input output is a method to make the intermediary data of the program to persist for the specific time period 
# whatever the time period can be 
# actually it is a method of file handling 
# Actually there are two types of files 
# 1. text files (.txt, .c)
# 2. Binary files (.jpg, .dat etc )
# python has lot of functions for the updating , deleting and inserting the content into the file already 
# exidting
# Openning the existing file 
# f = open ("file_name", "mode")
# mode can be write, read or update or etc by default it is read like "r" so if you want to read the content 
# there is no need to type the complete syntax involving the mode too by default it will take you to the read 
# mode
f = open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/file.txt")
data = f.read()
print(data)
f.close()
# now another mode exist which is the write mode presented as the 'w', we will be writing it like
# this will automatically write the the content into the opened file
str= "My name is Zeeshan Ali"
f = open("C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/09._Chapter 09/intro.txt","w")
f.write(str)
f.close()

# now we will be looking towards the readlines() function




 
