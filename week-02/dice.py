# We have 2 dice
# Throw the dice for the user and for the computer and find the winner

# I will use a LIBRARY
import random

user_1 = random.randint(1, 6)
user_2 = random.randint(1, 6)

computer_1 = random.randint(1, 6)
computer_2 = random.randint(1, 6)

print("USER: ", user_1, user_2)
print("COMPUTER: ", computer_1, computer_2)

user = user_1 + user_2
computer = computer_1 + computer_2

if user > computer:
    print("USER Wins")
elif computer > user:
    print("COMPUTER Wins")
else:
    print("It's a TIE")
