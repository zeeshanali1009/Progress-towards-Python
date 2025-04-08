# This program stores the multiplication table in the file 
# Write a program to print the table of a given number

n= int(input("Enter the number for which you want the multiplication table: "))

table =  [n*i for i in range(1,11)]
with open("c:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/12._Chapter 12 Practice/table.txt","a") as f:
    f.write(f"Table of {n} : {str(table)} \n")
print(table)