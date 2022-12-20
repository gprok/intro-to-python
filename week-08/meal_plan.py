import random

appetizers = ['pie', 'soup', 'yogurt', 'cheese']
main_dishes = ['beef', 'chicken', 'fish', 'lamp', 'pork', 'lentils']
salads = ['tomato', 'greens', 'cabbage']
deserts = ['ice cream', 'cake']

ap = appetizers[random.randint(0, len(appetizers)-1)]
print("Appetizer:", ap)

md = main_dishes[random.randint(0, len(main_dishes)-1)]
print("Main Dish:", md)

s = salads[random.randint(0, len(salads)-1)]
print("Salad:", s)

d = deserts[random.randint(0, len(deserts)-1)]
print("Desert:", d)
