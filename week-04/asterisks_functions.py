# ask user for a number N
# then print N asterisks
# e.g. if N=5 print *****

def print_asterisks(n, sep):
    for i in range(n):
        print("*", end=sep)
    print()


n = input("Please give a number: ")
n = int(n)

# i will take values from 0 to n-1
print("Print N asterisks")
print_asterisks(n, '-')

# Now I want a triangle of asterisks.
# e.g. if N = 5
# *
# * *
# * * *
# * * * *
# * * * * *
print("Print a Triangle")
for line in range(1, n+1):
    print_asterisks(line, ' ')
