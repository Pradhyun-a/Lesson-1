s1 = int(input("Enter your subject marks: "))
s2 = int(input("Enter your subject marks: "))
s3 = int(input("Enter your subject marks: "))
s4 = int(input("Enter your subject marks: "))
s5 = int(input("Enter your subject marks: "))

average = (s1 + s2 + s3 + s4 + s5) /5
print(average)

if average >=91 :
    print("Grade A1 ")
elif average >=81 :
    print("Grade A2 ")
elif average >=71 :
    print("Grade B1 ")
elif average >=61 :
    print("Grade B2 ")
elif average >=51 :
    print("Grade C1 ") 
else:
    print("Fail")                   