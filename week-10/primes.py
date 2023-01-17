
x = int(input("Give a number "))

p = True # flag to indicate if x is prime, I assume that it is prime
for n in range (2, x):
    if x % n == 0:  # not a prime
        p = False
        break

if p:
    print(x, "is Prime")
else:
    print(x, "is not Prime")


def is_prime(num):
    prime = True  # flag to indicate if x is prime, I assume that it is prime
    for n in range(2, num):
        if num % n == 0:  # not a prime
            prime = False
            break
    if prime:
        return True
    else:
        return False

for value in range(1, 1001):
    if is_prime(value):
        print(value)