# Write a program to find the greatest of given three numbers 

def greatest(a,b,c):
    if(a>b and a >c ):
        print(f"{a} is the greatest of all the given numbers ")
    elif(b>a and b > c):
        print(f"{b} is the greatest of all the given numbers ")
    elif(c>a and c > b):
        print(f"{c} is the greatest of all the given numbers ")

greatest(12,45,56)

        
