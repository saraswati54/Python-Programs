hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <=40:
    print(h * r)
elif h > 40:
    print(40* r + (h-40)*1.5*r)    

    # h-40 is for substraction then you get how many time you work extra for an get extra pay 