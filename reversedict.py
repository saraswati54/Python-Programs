
dict1 = {'a':1 , 'b':2}
#dict2 = (map(reversed, dict1.items()))
dict2 = {v: k for k,v in dict1.items()}
print(dict2)