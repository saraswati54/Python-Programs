import re
x = '123-45-6789'
#y = re.findall('^\d{3}-\d{2}-\d{4}$',x)
##y = re.findall("^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$",x)
y = re.findall("^\d{3}-?\d{2}-?\d{4}$",x)
print(y)

#x = 'from : Using the : character'
