# loops are used to make the iterations to do a single task multiple times 
# there are two types of loops :
# for loop
# while loop

# while loop works on the basis of condition it will continue to execute the statements present in the body
# multiple times untill the condition is satisfied

# i=0
# while (i<10):
#     print (i)
#     i +=1

# whenever the condition gets unsatisfied the loop will be exhausted 

# while loop can also be used to print the content of the list, tuple (iteratables)

l = [12,"Zeeshan"]
i=0
while (i<len(l)):
    print(l[i])
    i+=1
else:
    print("done")



