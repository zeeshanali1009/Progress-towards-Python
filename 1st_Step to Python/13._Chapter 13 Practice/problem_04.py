# write a program to filter the number only divisible by 5 

def divisible_by_5(n):
    if (n%5==0):
        return True
    return False

this_list = [12,45,67,79,34,2,68,89,45,78,34,79,34,2323,56,]
result = list(filter(divisible_by_5,this_list))
print(result)