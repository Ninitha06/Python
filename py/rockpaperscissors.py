import random


options = ["Rock", "Paper", "Scissors"]
computer = options[random.randint(0, 2)]
print(computer)

player = False
while (player == False):
    player = input("Rock, Paper, Scissors?? ")
    if (computer == player):
        print("Tie!!!")
    elif player == "Rock":
        if computer == "Paper":
            # Automatically displays output with space seperator
            print("You Lose!!!", computer,"covers",player)
        else:
            print("You Win!!!",player,"smashes",computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!!!",computer,"cut",player)
        else:
            print("You Win!!!",player,"covers",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!!!" + computer + " smashes " + player)
        else:
            print("You Win!!!" + player + " cut " + computer)
    else:
        print("Invalid Play. Please check your spelling")
    player = False
    computer = options[random.randint(0,2)] 