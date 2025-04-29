# This program adds up the real and imaginary parts of the two vectors and multiply them too

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i 
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self,c2):
        real_part = self.r + c2.r - self.i * c2.i
        img_part = self.r * c2.i - self.i * c2.r
        return Complex(real_part,img_part)
    
    
    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(1,2)
c2 = Complex(4,5)
print(c1+c2)
print(c1*c2)
        