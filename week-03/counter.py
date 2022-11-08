# Ask user for a number and count from 0 to this number

n = input("Give a number: ")
n = int(n)

counter = 0
while counter <= n:
    print(counter)
    counter = counter + 1

# another type of loop is for
for counter in range(n+1):
    print(counter)

# find sum of number 0 to n
counter = 0
total = 0
while counter <= n:
    total = total + counter
    counter = counter + 1
print("TOTAL:", total)
