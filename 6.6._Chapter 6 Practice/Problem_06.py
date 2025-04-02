# Write a program to allot the grade to the student according to the following scheme
# 90-100 Ex
# 80-90 A
# 70-80 B
# 60-70 C
# 50-60 D
# 40-50 F

user_input = input("Enter the name: ")
user_marks = int(input("Enter your marks: "))

if user_marks >= 90 and user_marks <= 100:
    print("Student Grade : Excellent!")
elif user_marks >= 80 and user_marks <= 90:
    print("Student Grade : A!")
elif user_marks >= 70 and user_marks <= 80:
    print("Student Grade : B!")
elif user_marks >= 60 and user_marks <= 70:
    print("Student Grade : C!")
elif user_marks >= 50 and user_marks <= 60:
    print("Student Grade : D!")
elif user_marks < 50:
    print("Student Grade : Fail!")

