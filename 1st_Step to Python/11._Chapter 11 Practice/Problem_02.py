# This program creates a class Animal then the pet class and then the dog class and then add the 
# function bark in the dog class 
 
class Animals:
    pass 
class  Pets(Animals):
    pass
class Dogs(Pets):
    @staticmethod
    def bark():
        print("Just wow!")

a = Dogs()
a.bark()
