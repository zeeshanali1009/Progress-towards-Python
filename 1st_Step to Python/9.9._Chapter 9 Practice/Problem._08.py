# This program generates the copy of the exixting file 

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/file_to_be_copied.txt') as f:
    content  = f.read()

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/file_to_be_copied_01.txt', 'w') as f:
    f.write(content)