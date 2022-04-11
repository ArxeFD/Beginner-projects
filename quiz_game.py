point = 0

print("Welcome to my Quiz Game!")

playing = input("Do you wanna play? ").lower()
if playing != "yes":
    quit()

print("Then let's head on!")

question = input("Do you belive in god? ").lower()
if question == "no":
    print("Incorrect!")
    point = (point - 1)
elif question == "yes":
    print("Correct!, you got 1 point!")
    point = (point + 1)
else:
    print("You must be devoted. I'ts Yes or anything! >:(")

question = input("You got money? ").lower()
if question == "no":
    print("Incorrect!")

elif question == "yes":
    print("Correct!, you got 1 point!")
    point = (point + 1)

question = input("Do you belive in satan? ").lower()
if question == "yes":
    print("Incorrect!")
elif question == "no":
    print("Correct!, you got 1 point!")
    point = (point + 1)

question = input("Cats or dogs? ").lower()
if question == "cats" or "dogs" or str :
    print("Every answer is accepted in this one!\nYou got one point!")
    point = (point + 1)

print("you got", point, "out of 4 points!")