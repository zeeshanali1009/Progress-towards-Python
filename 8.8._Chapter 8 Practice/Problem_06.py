# Write a program to convert the inches into cms  i.e temperature conversions 
def inches_to_cms(inch):
    return (inch*2.54)

user_input = int(input("Enter the number of inches: ")) 
result = inches_to_cms(user_input)
print(f"The number of centimeters will be {result}")
