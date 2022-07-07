
a = ['a','b','c','d']
b = enumerate(a)
print(b+1)
d = dict((i,j) for i,j in b)

#d= {tuple(key): idx for  idx, key in enumerate(a)}
print(d)
