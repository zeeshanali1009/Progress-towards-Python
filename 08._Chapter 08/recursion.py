# Recursion is also one of the most important part of the programming as it helps to give the important 
# functionality in few line of codes 

def fictorial(n):
    if n==0 or n==1:
        return 1
    return n* fictorial(n-1)


n= int(input("Enter the number: "))
print (f"Fictorial of the given number is : {fictorial(n)}")
