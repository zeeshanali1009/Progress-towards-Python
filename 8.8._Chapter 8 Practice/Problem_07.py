# Write a program to remove the particular word form the list 

# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l
    
# l= ["Zeeshan", "Zain", "Zohaib", "Zo"]
# print(rem(l,"Zo"))

# Now ad strip into the content of the list too

def rem(l,word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    
l= ["Zeeshan", "Zain", "Zohaib", "Zo"]
print(rem(l,"Zo"))