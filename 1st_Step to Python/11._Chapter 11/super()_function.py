# In this part we will be discussing about the super function 
# Inheritance is the most important property of the oop
# There are different types of inheritance in this section we will be discussing the single level inheritance
class Demo:
    def __init__(self):
        print("This is the base class constructor!")
    demo_attribute = "demo value"
    

class Second_Demo(Demo):
    def __init__(self):
        super().__init__()            # this will call the constructor of parent class too
        print("This is the derived class constructor!")
    Second_demo_attribute = "Second demo value"

obj_01 = Second_Demo
print(obj_01.demo_attribute , obj_01.Second_demo_attribute)
# obj_01.demo_property()

