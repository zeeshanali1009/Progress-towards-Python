#  in this part we will be discussing the operater overloading 
class Number:
    a =1
    b=2

    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    
a = Number(1)
b = Number(2)

print(a+b)