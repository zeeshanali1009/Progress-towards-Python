# This program check the prefernce between the class attribute and the instance attribute 

class demo:
    demo_attribute= "demo value"

demo_object=  demo()
print(demo_object.demo_attribute)

demo_object.demo_attribute= "double demo value"
print(demo_object.demo_attribute)

# Here one thing is very much notable and it is in second print call we have used the instance attribute and 
# apparently it is seen that the instance attribute changes the value of the class attribute too but it is not
# # true it just creates an other instance with the updated Value

print(demo.demo_attribute)
print("hence it is proved! Instance atribute just creates the instance.")


