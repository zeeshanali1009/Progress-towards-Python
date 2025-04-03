# Write a program to convert the fehrernhite into celcius  i.e temperature conversions 
def temp_convert(fehrenhite):
    return 5*(fehrenhite-32)/9

user_input = int(input("Enter the temperature into fehrenhite: ")) 
result = temp_convert(user_input)
print(f"{round(result,2)}°C")
