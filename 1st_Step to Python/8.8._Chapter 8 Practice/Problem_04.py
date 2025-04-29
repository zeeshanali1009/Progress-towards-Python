# Write a program to print the sum of first 10 natural numbers using recurrsion

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))