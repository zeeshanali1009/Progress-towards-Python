# """
# A class representing a student with name, class, and roll number.
# It includes a method to display the student's information.
# """
class Student:
    name = "Zeeshan"                                  # Class Attribute: Default student name
    s_class = "Intermediate"                            # Class Attribute: Default student class
    roll_no = "056"                                    # Class Attribute: Default student roll number

    def __init__(self):
        print("I am the default constructor!")

    def __init__(self,name,s_class,roll_no):         # dunder method will be called automatically when starts with
        self.name=  name                                #__
        self.s_class=  s_class
        self.roll_no=  roll_no

        
# Prints the student's name, class, and roll number.
# The 'self' parameter refers to the instance of the class.
       
    def Std_info(self):
        print("This function contains the details of the student")
        print(f"Student Name: {self.name}  Student Class:  {self.s_class}  Student Roll no : {self.roll_no}")
    
    @staticmethod               # this statement has been used for removing the use of "self"
    def greet():
        print("Hello Students!")


obj_01 = Student("Zeeshan", "Intermediate", 12,)
print(obj_01.name, obj_01.roll_no)


        




