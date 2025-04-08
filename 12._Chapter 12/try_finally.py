# in this section we will be discussing the use of try statement with the finally statement
# in the whole scenario the finally statement is always executable if the try statement was successfull or 
# not
def func_1():
    try: 
        a = int(input("Enter the number: "))
        print(a)

    except Exception as e:
        print(e)
        print("Exception case error")

    finally:
        print("I am inside the else and the try statement was executed successfully")

func_1()
