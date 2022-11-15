# I ask user for a word
# then ask for a letter
# I want to check if the word contains the letter
# if word=mississippi and letter=a => "a not in mississippi"
# if word=mississippi and letter=p => "p is in mississippi"


# get word
word = input("Give a word: ")

# get letter
letter = input("Give a letter: ")

flag = False
# for every char in the word
for char in word:
    # if char is equal to letter we have it
    if char == letter:
        print(letter + " is in " + word)
        flag = True
        break

if flag is False:
    print(letter + " not in " + word)

