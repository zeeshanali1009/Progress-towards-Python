# Inheritance is the most important property of the oop
 

class Demo:
    demo_attribute = "demo value"

    def demo_property(self):
        print(f"This is the demo property with the demo attribute like : {self.demo_attribute}")

class Second_Demo(Demo):
    demo_attribute = "demo value"

    def demo_property(self):
        print(f"This is the demo property with the demo attribute like : {self.demo_attribute}")

# This is the simple approach 
obj_01 = Demo()
print(obj_01.demo_attribute)
obj_01.demo_property()

obj_02 = Second_Demo()
print(obj_01.demo_attribute)
obj_01.demo_property()

# This approach can make the code very hard to understand and a complex one so the approach of 
# inheritance is being used to improve the readability of the code and make it more understandable
    