# ask user for a number N
# then print N asterisks
# e.g. if N=5 print *****

n = input("Please give a number: ")
n = int(n)

# i will take values from 0 to n-1
print("Print N asterisks")
for i in range(n):
    print("*", end=' ')
print()

# Now I want a triangle of asterisks.
# e.g. if N = 5
# *
# * *
# * * *
# * * * *
# * * * * *
print("Print a Triangle")
for line in range(1, n+1):
    for i in range(line):
        print("*", end=' ')
    print()
