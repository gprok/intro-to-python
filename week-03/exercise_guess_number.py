# Set a secret random number N
# Loop until user finds the number
# Ask the user to guess the number
# if guess < N say GO UP
# if guess > N say GO DOWN
# if guess == N the loop will stop and say THAT'S IT!

# New feature: count number of guesses until found

import random

secret = random.randint(1, 100)

found = False
counter = 0

while not found:
    n = input("Guess: ")
    n = int(n)
    counter = counter + 1
    if n < secret:
        print("GO UP")
    elif n > secret:
        print("GO DOWN")
    else:
        print("THAT'S IT!")
        found = True

print("Found in", counter, "guesses")
