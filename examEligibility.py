medicalCause = input("Do you have a medical condition, (Y/N): ")
if medicalCause == "Y" :
    print("Your are allowed to take the test ")
else :
    attendance = int(input("Enter your attendance percentage: "))
    if attendance >= 75 :
        print("You are allowed to take the exam ")
    else :
        print("You are not allowed to take the exam ")    