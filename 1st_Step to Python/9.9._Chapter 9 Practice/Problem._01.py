# This program checks whether the specific word is present in the other file or not 
f = open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/01._file.txt')
content = f.read()
if "Intelligence" in content:
    print("The word Intelligence is present in the file.")
else:
    print("The word Intelligence is not present in the file.")
