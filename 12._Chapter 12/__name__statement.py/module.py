# this is the main file 

def func():
    print("This is the function")


# below given code is safe from the execution effect of the other file naming "main"
# this is what we get as the security in the advance python
if __name__ == "__main__" :
    print("We are directly running this code")
    func()
    print(__name__)


