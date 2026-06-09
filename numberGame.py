import random

integer = random.randint(1, 5)
user = int(input("Enter an integer: "))

if integer == user:
    print("Congratulations you guessed correctly! ")
else:
    print("Sorry, you have guessed wrong ")

print("Computer selected: ", integer)
