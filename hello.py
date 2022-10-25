name = input("Type your name: ")
age = int(input("Your age: "))

print("Hello " + name + ", you are " + str(age) + " y.o.")

if age < 18:
    print("Sorry, you cannot enter")
else:
    print("OK to enter")
