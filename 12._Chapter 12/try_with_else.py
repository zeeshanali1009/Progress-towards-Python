# in this section we will be discussing the use of try statement with the else statement
# in the whole scenario the else statement is only executable if the try statement was successfull
try: 
    a = int(input("Enter the number: "))
    print(a)

except Exception as e:
    print(e)
    print("Exception case error")
else:
     print("I am inside the else and the try statement was executed successfully")
