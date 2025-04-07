# In this part we will be discussing about the property decorater 

class Demo:
    demo_attribute = "demo value"

    @property
    def name(self):
        return f"{self.fname}  {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
obj_01 = Demo()
obj_01.name = "Zeeshan Ali"
print(obj_01.fname, obj_01.lname)


# here it is the best examle of abstraction and encapsulation because user do not know that his name has 
# been splitted into fname and lastname