    # """
    # A class representing a student with name, class, and roll number.
    # It includes a method to display the student's information.
    # """
class Student:
    name = "Zeeshan"                                  # Class Attribute: Default student name
    s_class = "Intermediate"                            # Class Attribute: Default student class
    roll_no = "056"                                     # Class Attribute: Default student roll number

        # """
        # Prints the student's name, class, and roll number.
        # The 'self' parameter refers to the instance of the class.
        # """
    def Std_info(self):
        print("This function contains the details of the student")
        print(f"Student Name: {self.name}  Student Class:  {self.s_class}  Student Roll no : {self.roll_no}")
    
    @staticmethod               # this statement has been used for removing the use of "self"
    def greet():
        print("Hello Students!")



std_01 = Student() 
std_01.name = "Ali" 

# below given both the statements have the same purpose they will do the same task
std_01.Std_info()   
# Student.Std_info(std_01)     

std_01.greet() 


        




