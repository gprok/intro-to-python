
grades = [90, 82, 76, 88, 90, 92]

print(grades)
print(len(grades))

for g in grades:
    print(g)

# i will take values from 0 to (length of the list - 1)
for i in range(len(grades)):
    print(i, grades[i])

# Find the Average grade:
total = 0
for g in grades:
    total = total + g
print("Total", total)
print("Average", total/len(grades))

# EXERCISE: Can you find the MAX and the MIN grade?
min = grades[0]
max = grades[0]
for g in grades:
    if g > max:
        max = g
    if g < min:
        min = g
print("MAX:", max)
print("MIN:", min)

grades.sort()
print(grades)
print("MIN:", grades[0])
print("MAX:", grades[-1])
