try:
    num = int(input("Enter a number "))
    print(num)
except ValueError:
    print("Enter a different number ")
finally:
    print("The code will always print ")
