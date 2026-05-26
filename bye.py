valid = False
while not valid:
    try:
        num = int(input("Enter a number: "))
        valid = True
        if num % 2 == 0:
            while True:
                print("Bye ")
        else:
            print("The number is not divisible by 2 ")
    except ValueError:
        print("Invalid input, please enter a number ")
