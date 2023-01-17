import random

numbers = []

repeat = "y"
while repeat == "y":
    n = random.randint(1, 100)
    print("Your number is: ", n)
    numbers.append(n)
    repeat = input("continue? (y/n) ")

# print all the collected numbers
for n in numbers:
    print(n, end=' ')
print()


# print the list sorted
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)




