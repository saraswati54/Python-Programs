
import re

email = "sammy@gmail.com"
#y = re.findall(r'([\w.-]+)@gmail.com',email)
y = re.findall( '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)
print(y)