# In this part we will be discussing the object oriented programming 
class Student:
    name = "Zeeshan"                            # Class Attributes
    s_class = "Intermediate"                            # Class Attributes
    roll_no = "056"                         # Class Attributes
#  So that was how the class will be created
# now we will call it using the object or instance 

zeeshan = Student()
print(zeeshan.name, zeeshan.s_class , zeeshan.roll_no)       # class attributes 

# Instance/Object Attributes
zeeshan.marks  = 100
print(f"Zeeshan Marks : {zeeshan.marks}")

# Now we will be checking the prefernece of the attributes 
# Class Attributes vs Instance Attributes 
zeeshan.roll_no = 18
print (f"Zeeshan Roll no : {zeeshan.roll_no}")
# hence proved that instance attribute prefernce is higher then the class attribute 


