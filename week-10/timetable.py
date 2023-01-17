Day = input("What day are you looking for?")
Lesson = int(input("What lesson are you looking for?"))
if Day == "Monday":
    Monday = ["Humanities", "Science", "P.E.", "Computer Science", "Math", "English"]
    print(Monday[Lesson - 1])
if Day == "Tuesday":
    Tuesday = ["Computer Science", "French", "Math", "Science", "Humanities", "PSHE"]
    print(Tuesday[Lesson - 1])
if Day == "Wednesday":
    Wednesday = ["Music", "Humanities", "English", "French", "Science", "Drama"]
    print(Wednesday[Lesson - 1])
if Day == "Thursday":
    Thursday = ["Music", "French", "P.E.", "Enrichment", "Math", "English"]
    print(Thursday[Lesson - 1])
if Day == "Friday":
    Friday = ["Art", "Drama", "Science", "English", "Humanities", "Math"]
    print(Friday[Lesson - 1])
if Day == "Saturday":
    print("No lessons today!")
if Day == "Sunday":
    print("No lessons today!")
