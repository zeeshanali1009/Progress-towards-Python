# This program prints the word artificial with intelligence

word = "Intelligence"
with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/01._file.txt') as f:
    content = f.read()
    newcontent = content.replace(word, "Artificial")

with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/01._file.txt', 'w') as f:
    f.write(newcontent)