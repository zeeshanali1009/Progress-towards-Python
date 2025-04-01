# What will be the length of the following set
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# it is very interesting phenomena as apprantely it seems that the 20.0  and 20 are differnt values according
# to the python but they are not same python takes them same 
# 20.0 = 20
# these values are the same 

