import random
from time import sleep

list = ["rock", "paper", "scissors"]

play = input("Wanna play rock paper scissors? ").lower()

if play == "yes":
    print("So let's head on!")
else:
    print("Goodbye then...")
    quit()

sleep(1.2)
print("You'll have 3 tries!")

points = 0
tries = 0
while tries < 3:
    variable = random.choice(list)
    sleep(1.0)
    game = input("rock paper or scissors? ").lower()
    print("Computers choice is", variable)

    if variable == "scissors" and game == "scissors":
        print("It's a draw!")
        tries += 1
    elif variable == "scissors" and game == "paper":
        print("You lost!")
        tries += 1
    elif variable == "scissors" and game == "rock":
        print("You won!")
        tries += 1
        points += 1
    elif variable == "rock" and game == "scissors":
        print("You won!")
        tries += 1
        points += 1
    elif variable == "rock" and game == "paper":
        print("You lost!")
        tries += 1
    elif variable == "rock" and game == "rock":
        print("It's a draw!")
        tries += 1
    elif variable == "paper" and game == "scissors":
        print("You lost!")
        tries += 1
    elif variable == "paper" and game == "paper":
        print("It's a draw!")
        tries += 1
    elif variable == "paper" and game == "rock":
        print("You won!")
        tries += 1
        points += 1

print("Your score is", points, "out of 3")