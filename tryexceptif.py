Score= input("Enter Score:")
try:
   S=float(Score)
   if S<=1 or S>=0.0:
       print("Out of range")
   elif S>=0.9:
       print("A")
   elif S>=0.8:
       print("B")
   elif S>=0.7:
       print("C")	
   elif S>=0.6:
       print("D")	 
   elif S>=0.6:
       print("F")	   	   
except:
   print("Error")