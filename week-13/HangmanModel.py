from typing import List

from faker import Faker


class HangmanModel:
    def __init__(self):
        self.word = ''
        self.correct = []
        self.wrong = []

    def start(self):
        generator = Faker()
        while True:
            self.word = generator.word()
            print(self.word)
            if len(self.word) >= 6:
                break
        self.correct = []
        self.wrong = []

    def get_secret(self) -> str:
        secret = self.word[0]
        for i in range(1, len(self.word) - 1):
            if self.word[i] in self.correct:
                secret += self.word[i]
            else:
                secret += '_'
        secret += self.word[-1]
        return secret

    def play(self, letter):
        if letter in self.correct or letter in self.wrong:
            print(letter + " already guessed")
        else:
            if letter in self.word:
                # correct
                self.correct.append(letter)
            else:
                # wrong
                self.wrong.append(letter)

    def found(self):
        if self.word == self.get_secret():
            return True
        else:
            return False

    def hanged(self):
        if len(self.wrong) == 6:
            return True
        else:
            return False


hangman = HangmanModel()
hangman.start()
while True:
    print(hangman.get_secret())
    letter = input("Guess: ")
    hangman.play(letter)
    if hangman.found():
        print(hangman.word + " found!")
        break
    if hangman.hanged():
        print("You are hanged!")
        break


