# This program renames the file 
with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/file_to_be_renamed.txt') as f:
    content  = f.read()

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/renamed_file.txt', 'w') as f:
    f.write(content)

