import random

words = ["mississippi", "polymorphism", "empathy", "television", "internet"]

pos = random.randint(0, len(words)-1)

print(pos, words[pos])

found = []
not_found = []
w = words[pos]

while True:
    secret = w[0]
    for i in range(len(w)-2):
        if w[i+1] in found:
            secret = secret + w[i+1]
        else:
            secret = secret + '_'
    secret = secret + w[-1]

    # if all letters have been found display "YOU FOUND IT"
    if secret == w:
        print("WORD", w, "FOUND")
        break

    # update secret
    print("Secret", secret)

    # ask user for a letter
    letter = input("Give a letter: ")
    # if the letter is in w add it to a found list
    if letter in w:
        found.append(letter)
    # else add it to a not-found list
    else:
        not_found.append(letter)

    # if 6 letters are in not-found "GAME OVER"
    if len(not_found) == 6:
        print("GAME OVER")
        break
