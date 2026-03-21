print("Select your ride ")
print("1. Bike ")
print("2. Car ")

choice = int(input("Enter your choice: "))

if choice == 1 :
    print("Select bike type ")
    print("1. Scooter ")
    print("2. Sports bike ")
    bike = int(input("Enter your choice: "))

    if bike == 1 :
        print("You have selected a scooter ")
    else :
        print("You have selected a sports bike ")
elif choice == 2 :
    print("Select car type ")
    print("1. Sedan ")
    print("2. SUV ")
    car = int(input("Enter your choice: "))

    if car == 1 :
        print("You have selected a sedan ")
    else :
        print("You have selected a SUV ")
else: 
    print("Invalid choice ")                         