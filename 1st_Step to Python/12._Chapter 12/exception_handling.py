# In this part we will be discussing the use of try and except statements as 
try: 
    a = int(input("Enter the number: "))
    print(a)

except ZeroDivisionError as z:
    print(z)
    print("Zero division error")
except ValueError as v:
    print(v)
    print("Value error")
except Exception as e:
    print(e)
    print("Exception case error")

print("Thank you!")

# now the concept is try statement execution is completed, there will compiler will not execute the except
# statement as the except statement is the case for the exceptions
# now we will be discussing the different types of the exceptions   