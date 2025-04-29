# Write a program to print the following pattern 
#*
#***
#****


user_input = int(input("Enter the number to initiate the pattern: "))
for i in range(1,user_input+1):
    print("*" *(i),end = "")
    print(" ")