# This progrsm check the log file and search out whether the python i present in the log file or not

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/log_file.html', 'r') as f:
    content = f.read()

if ("Python" in content):
    print("Python is present in the log file.")
else:
    print("Python is not present in the log file.")
    