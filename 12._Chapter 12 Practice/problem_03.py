# Write a program to print the table of a given number

n= int(input("Enter the number for which you want the multiplication table: "))

table =  [n*i for i in range(1,11)]
print(table)