# This progrsm check the log file and search out whether the python i present in the log file or not
# Write a program and find where the python word is present 

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/log_file.html', 'r') as f:
    lines  = f.readlines()

lineno =1
for line in lines:
    if ("Python" in lines):
        print(f"Python is present in the log file. {lineno}")
        break
    lineno +=1


else:
    print("Python is not present in the log file.")
    