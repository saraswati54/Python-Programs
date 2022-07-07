
score = float(input("Enter score: "))

if 0.0 > score > 1.0:
    print("Score is out of range") 
elif score >= 0.9:
    print("Grade A")
elif 0.9 > score >= 0.8:
    print("Grade B")
elif  0.8 > score >= 0.7:
    print("Grade C")
elif 0.7 > score >= 0.6:
    print("Grade D")
else: 
    print("F")

    




