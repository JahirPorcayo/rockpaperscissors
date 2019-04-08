from random import *
items = ['rock', 'paper', 'scissors']
# x is player 2
player2 = sample(items, 1)[0]
# print(player2)


# print("Rock....")
# print("paper....")
# print("scissors....")

player1 = input("player 1, make your move: ")
# check player one chooses an item
# print("No cheating\n" * 20)
# player2 = input("player 2, make your move: ")


if player1 == player2:
    print("its a tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("player 1 wins")
    elif player2 == "paper":
        print("player2 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    elif player2 == "scissors":
        print("player2 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins")
    elif player2 == "paper":
        print("player1 wins")
else:
    print("somethinfg wrong")
