# This program prints the list of words with the # the number of letters there are in the list

words = ["Intelligence", "Intelligent", "Brilliant"]
with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/01._file.txt', 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"* len(word))


with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/01._file.txt', 'w') as f:
    f.write(content)