# match case in the python is just like the switch statement in other programming languages
# Find the number 500 from the user
def finding_number(number):
    match number:
        case 100:
            return "You entered the 100"
        case 200:
            return "You entered the 200"
        case 300:
            return "You entered the 300"
        case 400:
            return "You entered the 400"
        case 500:
            return "You entered the 500! Right Number."
        case _:
            return "Unknown Number!"
        
print(finding_number(100))
print(finding_number(200))
print(finding_number(300))
print(finding_number(400))
print(finding_number(500))

# So that was the use case 


