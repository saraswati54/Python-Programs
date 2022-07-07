""""
total = int(input('What is the total amount for your online shopping?'))
country = input('Shipping within the US or Canada?')
if country == "US":
    if  total < "50":
        print("Shipping Costs $6.00") 
    elif "50" <= total <= "100":
         print("Shipping Costs $9.00")
    elif "100"<= total <= "150":
         print("Shipping Costs $12.00")
    else:
         print("FREE")
#if country == "Canada":
else :
    if  total < "50":
        print("Shipping Costs $6.00") 
    elif "50" <= total <= "100":
         print("Shipping Costs $9.00")
    elif "100"<= total <= "150":
         print("Shipping Costs $12.00")
    else:
         print("FREE")
"""
total = int(input('What is the total amount for your online shopping?'))
country = input('Shipping within the US or Canada?')
if country == "US":
    if  total < 50:
        print("Shipping Costs $6.00") 
    elif 50 <= total <= 100:
         print("Shipping Costs $9.00")
    elif 100<= total <= 150:
         print("Shipping Costs $12.00")
    else:
         print("FREE")
#if country == "Canada":
else :
    if  total < 50:
        print("Shipping Costs $6.00") 
    elif 50 <= total <= 100:
         print("Shipping Costs $9.00")
    elif 100<= total <= 150:
         print("Shipping Costs $12.00")
    else:
         print("FREE")         