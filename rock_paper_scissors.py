import random
from time import sleep

list = ["rock", "paper", "scissors"]

play = input("Wanna play rock paper scissors? ").lower()

if play == "yes":
    print("So let's head on!")
else:
    print("Goodbye then...")
    quit()

sleep(0.8)
print("You'll have 3 tries!")

points = 0
tries = 0
while tries < 3:
    variable = random.choice(list)
    sleep(0.8)
    game = input("rock paper or scissors? ").lower()
    print("Computers choice is", variable)
    tries += 1

    if game == "rock" and variable == "scissors":
        print("You won!")
        points += 1
    elif game == "scissors" and variable == "paper":
        print("You won!")
        points += 1
    elif game == "paper" and variable == "rock":
        print("You won!")
        points += 1
    elif game == variable:
        print("Draw!")
    else:
        print("You lose!")

print("Your score is", points, "out of 3")