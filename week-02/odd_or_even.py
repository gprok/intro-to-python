# Ask user for a number and check if it is odd or even

# Get a number from the user
n = input("Give an integer: ")

try:
    # Convert it to an int
    n = int(n)

    # check if the number is even (operator % gives the remainder of the division) n % 2 == 0
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Please give integer values only")



