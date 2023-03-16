from typing import List

from faker import Faker


def get_secret(w: str, cor: List) -> str:
    secret = w[0]
    for i in range(1, len(w)-1):
        if w[i] in cor:
            secret += w[i]
        else:
            secret += '_'
    secret += w[-1]
    return secret


generator = Faker()
correct = []
wrong = []

while True:
    word = generator.word()
    print(word)
    if len(word) >= 6:
        break

while True:
    print(get_secret(word, correct))

    letter = input("Guess: ")
    if letter in correct or letter in wrong:
        print(letter + " already guessed")
    else:
        if letter in word:
            # correct
            correct.append(letter)
        else:
            # wrong
            wrong.append(letter)

    # check if found
    if word == get_secret(word, correct):
        print(word + " found!")
        break

    # check if hanged
    if len(wrong) == 6:
        print("You are hanged!")
        break



