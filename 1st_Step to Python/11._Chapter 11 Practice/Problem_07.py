# override the existing function and pass the list to the constructor 
class Vector:
    def __init__(self, list):
        self.x, self.y, self.z = list
    
    def __add__(self, other):
        return Vector([self.x + other.x, self.y + other.y, self.z + other.z])
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"Vector ({self.x}i , {self.y}j , {self.z}k)"
    
    def __len__(self):
        return 3
    

v1 = Vector([1, 2, 3])
print(len(v1))         # Output: 3
print(v1)              # Output: Vector (1i , 2j , 3k)

