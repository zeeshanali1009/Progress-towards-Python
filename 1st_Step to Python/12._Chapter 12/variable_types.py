# In this program we are discussing the role of the type definition in the program like 
from typing import List,Tuple,Dict,Union
number :int = 12

name : str = "Zeeshan"

def sum(a :int , b :int) -> int:
    return a+b

print(sum(12,12))

# As it has been clarified that clearifying the function definition early makes the process easier and then
# when we call the function the hints comes in front of us like what is the type of variables and what will
# the funtion return

# now the same process of type definitions for the list, tuples etc 

# it specifies that the numbers list has the type of integers 
numbers : List[int] = [12,34,556,87,89]
# it specifies that the breed tuple can have the both of the types like strings and the integers 
breed : tuple[str,int] = ["Freian", 5]
# it specifies that the dictionary can have the both of the types of strings and the integers 
marks : dict[str,int] = {"Zeeshan": 56 , "Muhammad": 90}
# it specifies that the variable can have the both of the types of strings and the integers 
# mixed_numbers = Union[int,str] = "ID123"


