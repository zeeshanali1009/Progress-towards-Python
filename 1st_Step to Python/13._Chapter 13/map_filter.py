from functools import reduce
# map example as follow 
# used to make something from the existing content 
this_list = [1,2,3,4,5,6]
square = lambda x: x*x

sqlist = map(square, this_list)
print(list(sqlist))

# example of filter as follow 
# it is used to filter some particular thing from the data
def even(n):
    if (n%2 ==0):
        return True
    return False

only_even = filter(even,this_list)
print(list(only_even))

# example of reduce function as follow:
# used to buckle up or reduce something from the data 
def sum(a,b):
    return a+b

mutiply_num = lambda x,y: x*y

print(reduce(sum,this_list))
print(reduce(mutiply_num,this_list))