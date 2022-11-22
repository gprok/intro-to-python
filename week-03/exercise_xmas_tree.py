# Ask user for a number N (N must be odd)
# print a Xmas tree of base N
# Example, for N=7, print
#       *
#     O * *
#   * * * O *
# * O * * * * *
#       #

# EXERCISE: Modify print_asterisk function to print random O instead of asterisk
# O is the Xmas tree balls!

def print_spaces(s):
    for i in range(s):
        print("  ", end="")


def print_asterisks(a):
    for i in range(a):
        print("* ", end="")


n = input("Give an odd number: ")
n = int(n)

if n % 2 == 0:
    print("Number is even, cannot create a tree")
else:
    rows = n // 2 + 1
    asterisks = 1
    spaces = n // 2
    for r in range(rows):
        # print spaces spaces
        print_spaces(spaces)
        # print asterisk asterisks
        print_asterisks(asterisks)
        # go to the next line
        print()
        # print(spaces, asterisks)
        asterisks = asterisks + 2
        spaces = spaces - 1
    print_spaces(n//2)
    print('#')