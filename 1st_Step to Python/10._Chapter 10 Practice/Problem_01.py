# Create a class Programmer and store the data of the programmers working at the microsoft 

class Programmers:
    Name = ""
    Address= ""
    City = ""

    def __init__(self,Name, Address, City):
        self.Name= Name
        self.Address= Address
        self.City= City

std_01= Programmers("Zeeshan", "Lahore", "Krk,Lahore")
print(std_01.Name,std_01.Address,std_01.City)
std_01= Programmers("Ali", "Karachi", "Sadar,Karachi")
print(std_01.Name,std_01.Address,std_01.City)
std_01= Programmers("Muhammad", "Faislabad", "Jaranwala,Faislabadd")
print(std_01.Name,std_01.Address,std_01.City)
        


