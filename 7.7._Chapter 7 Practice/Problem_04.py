# write a program to check whether the given number is prime or not 

user_input = int(input("Enter the number: "))
for i in range(2,user_input):
    if(user_input%i):
        print("Number is not prime!")
        break
else:
    print("Number is prime!")

