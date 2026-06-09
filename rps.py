import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock, paper, or scissors: ")

print("Computer selected: ", computer)

if user == computer:
    print("You have guessed correctly ")
else:
    print("You have guessed wrong ")
