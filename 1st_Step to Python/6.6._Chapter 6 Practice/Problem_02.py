# Write a program to check whether the student is pass or fail based on the following criteria 
# each subject marks must be greater then 40 and total marks must be greater then 33 inputing the marks of 
# three subjects 

user_name  = input("Enter the name of user : ")
subj_1 = int(input("Enter the marks of first subject"))
subj_2= int(input("Enter the marks of second subject:"))
subj_3= int(input("Enter the marks of third subject:"))

total = subj_1+ subj_2 + subj_3

if (total>=33 and subj_1>40 and subj_2>40 and subj_3>40):
    print("Student is Pass!")
else:
    print("Student is Failed")