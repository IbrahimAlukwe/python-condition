
marks = float(input("enter the marks"))

if marks > 90:
    print ("Grade O")
elif marks >= 80 and marks < 90:
    print ("Grade A+")
elif marks >= 70 and marks < 80:
    print ("Grade A")
elif marks > =60 and marks < 70:
    print ("Grade B+")
elif marks >= 50 and marks < 60:
    print ("Grade B")
elif marks >= 40 and marks < 50:
    print ("Grade C+")
elif marks >= 30 and marks < 40:
    print ("Grade C")
elif marks >= 20 and marks < 30:
    print ("Grade E")
elif marks >= 10 and marks < 20:
    print ("Grade F")
elif marks >= 0 and marks < 10:
    print ("Grade F")

else: print ("Grade :F")