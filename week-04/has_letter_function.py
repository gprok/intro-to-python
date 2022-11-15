# I ask user for a word
# then ask for a letter
# I want to check if the word contains the letter
# if word=mississippi and letter=a => "a not in mississippi"
# if word=mississippi and letter=p => "p is in mississippi"


def has_letter(word, letter):
    # for every char in the word
    for char in word:
        # if char is equal to letter we have it
        if char == letter:
            return True
    return False


# get word
word = input("Give a word: ")

# get letter
letter = input("Give a letter: ")

if has_letter(word.lower(), letter.lower()):
    print(letter + " is in " + word)
else:
    print(letter + " not in " + word)

