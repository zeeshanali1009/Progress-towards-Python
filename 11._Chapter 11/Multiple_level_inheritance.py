# Inheritance is the most important property of the oop
# There are different types of inheritance in this section we will be discussing the Multiple level inheritance
class Demo:
    demo_attribute = "demo value"
    def demo_property(self):
        print(f"This is the demo property with the demo attribute like : {self.demo_attribute}")

class Second_Demo(Demo):
    Second_demo_attribute = "Second demo value"
    def Second_demo_property(self):
        print(f"This is the demo property with the demo attribute like : {self.demo_attribute}")

class Third_Demo(Second_Demo):
    Third_demo_attribute = "Third demo value"
    def Third_demo_property(self):
        print(f"This is the demo property with the demo attribute like : {self.Second_demo_property}")

obj_01 = Second_Demo
print(f"Here it can be seen that the secnd class instance is accessing the first class attribute : {obj_01.demo_attribute}")
# obj_01.demo_property()
Second_Demo.demo_property(obj_01)


obj_02 = Third_Demo
print(f"Here it can be seen that the secnd class instance is accessing the first class attribute : {obj_02.Second_demo_attribute}")
# obj_01.demo_property()
Third_Demo.Second_demo_property(obj_02)

