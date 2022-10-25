# Ask user for their name and gender
# Then say hello to the use with Mr or Mrs depending on the gender

name = input("Your name: ")
gender = input("Gender M/F: ")

if gender == 'M':
    print("Hello Mr.", name)
elif gender == 'F':
    print("Hello Mrs.", name)
else:
    print("Hello ", name)