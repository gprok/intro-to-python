print ("Welcome, please choose one of the options below.")
print ("1. KPH to MPH")
print ("2. MPH to KPH")
choice=input("1 or 2")
if choice == "1":
    kph=int(input("What speed are you travelling at?"))
    print ("You are traveling at", kph/1.6, "MPH")
elif choice == "2":
    mph=int(input("What speed are you travelling at?"))
    print ("You are traveling at", mph*1.6, "KPH")
else:
    print ("Not a valid entry")
