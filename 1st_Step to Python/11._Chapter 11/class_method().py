# In this part we will be discussing about the super function 
# Inheritance is the most important property of the oop
# There are different types of inheritance in this section we will be discussing the single level inheritance
class Demo:
    demo_attribute = "demo value"
    @classmethod
    def show(cls):
        print(f"value: {cls.demo_attribute}")
    
obj_01 = Demo()
obj_01.demo_attribute = 34
obj_01.show()

# class method do not allow to change the value of attribute 

