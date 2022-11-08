# Game Paper (1) Rock (2) Scissors (3)
# Ask user to select P(1), R(2), S(3)
# Then, produce a random value 1, 2, or 3 for the Computer
# Find and print the WINNER or TIE

# HINT: if user == 1 and computer == 2:
import random

play = "y"
while play == "y":
    # get user's input
    user = input("select Paper(1), Rock(2), Scissors(3): ")
    user = int(user)

    # calculate computer's choice as a random number
    computer = random.randint(1, 3)
    print("Computer selected:", computer)

    # find the winner
    # equal values is a TIE
    if user == computer:
        print("It's a TIE")
    # 1 wins 2
    elif user == 1 and computer == 2:
        print("User wins")
    elif computer == 1 and user == 2:
        print("Computer wins")
    # 2 wins 3
    elif user == 2 and computer == 3:
        print("User wins")
    elif computer == 2 and user == 3:
        print("Computer wins")
    # 3 wins 1
    elif user == 3 and computer == 1:
        print("User wins")
    elif computer == 3 and user == 1:
        print("Computer wins")

    play = input("Play again y/n: ")
    
print("GAME OVER")

