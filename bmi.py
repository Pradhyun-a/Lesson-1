weight = float (input ("Enter your weight in kg: "))
height = float (input( "Enter your height in m: "))
bmi = weight/(height**2)

if bmi < 18.5 :
    print("You are underweight ")

elif bmi < 25 :
    print("You are average weight ")

elif bmi < 30 :
    print("You are overweight ")

else :
    print("You are obese ")    
     