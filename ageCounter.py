try:
    age = int(input("Enter your age: "))
    
    if age % 2 == 0:
        print("The age is Even")
    else:
        print("The age is Odd")

except ValueError:
    print("Please enter a valid integer.")
