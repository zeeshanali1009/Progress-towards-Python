# This program checks whether the two identical files have the same content or not 
with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/file_to_be_copied.txt') as f:
    content_01  = f.read()

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/file_to_be_copied_01.txt') as f:
    content_02 = f.read()

    if (content_01 == content_02):
        print("The content is identical")
    else:
        print("The content is not identical")
