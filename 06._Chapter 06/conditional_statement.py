# in this section we will discuss about the conditional statements in the python as they plays an important 
# role in the decision making like not if so elif and not elif so else these are the ipmrtant terminologies
# for the process of decision making 

a = input ("Enter your age : ")
a_1 =  int(a)
if (a_1 <= 0):
    print ("This cannot be the age, age must be greater then 0")
elif a_1 < 18:
    print("You are not eligible for the National Identity Card")
elif a_1 >= 18:
    print("You are eligible for the National Identity Card")