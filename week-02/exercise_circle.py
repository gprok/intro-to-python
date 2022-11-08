# Ask user for radius of a circle (NOTE: radius can be decimal, convert to float(n))
# Calculate and print the Area and the Perimeter of the circle
# area = π * r to the power of 2
# perimeter = 2 * π * r

# 1. get number from the user
import math

n = input("Give radius: ")

# 2. convert user input to number
radius = float(n)

print("π:", math.pi)
# 3. calc and print area
area = math.pi * (radius ** 2)
print("Area:", area)

# 4. clac and print perimeter
perimeter = 2 * math.pi * radius
print("Perimeter:", perimeter)
