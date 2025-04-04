# This program prints the table from 2 to 20 

def generate_tables(n):
    table= ""
    for i in range(1,11):
        table+= f"{n} x {i} = {n*i}\n"
        with open(f'C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/03._tables/table_{n}.txt' , 'w') as f:
            f.write(table)




for i in range (2,21):
    generate_tables(i)

