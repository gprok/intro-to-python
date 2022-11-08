# Practice with arithmetic operations
# Ask user for 2 numbers a and b.
# Then calculate and print:
# - Sum, difference, product, result and remainder of the division, a to the power of b
# Also check which number is greater and print (A is grater or B is grater)

# Ask for 1st number and convert to int
a = input("Give A: ")
a = int(a)

# Ask for 2nd number and convert to int
b = input("Give B: ")
b = int(b)

# FInd sum
print("Sum:", a + b)

# difference,
print("Difference:", a - b)

# product,
print("Product:", a * b)

# result and remainder of the division,
print("Division:", a / b)
print("Remainder:", a % b)

# a to the power of b
print("Power:", a ** b)

# greater number
if a > b:
    print(a, "is greater")
elif a < b:
    print(b, "is greater")
else:
    print("number are equal")