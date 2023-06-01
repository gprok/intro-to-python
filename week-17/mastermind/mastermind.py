import random


class Mastermind:
    def __init__(self):
        # what variables we will need
        self.secret = []
        self.last_response = []
        self.responses = []
        self.feedbacks = []
        pass

    def play_again(self):
        self.secret = []
        self.last_response = []
        self.responses = []
        self.feedbacks = []

    def get_unique_random(self):
        while(True):
            n = random.randint(0, 9)
            if n not in self.secret:
                return n

    def set_secret(self):
        self.secret = []
        for i in range(4):
            n = self.get_unique_random()
            self.secret.append(n)
        print("Secret:", self.secret)

    def check_response(self, response):
        self.last_response = response
        for i in range(4):
            if self.secret[i] != response[i]:
                return False
        return True

    def get_feedback(self) -> []:
        feedback = []
        for i in range(4):
            if self.secret[i] == self.last_response[i]:
                feedback.append('r')
            elif self.last_response[i] in self.secret:
                feedback.append('w')
        self.responses.append(self.last_response)
        self.feedbacks.append(feedback)
        return sorted(feedback)


if __name__ == '__main__':
    found = False

    ### GET USER'S NAME

    game = Mastermind()
    # Calculate the secret
    game.set_secret()

    for i in range(12):
    # Repeat 12 times
        # Ask user to play
        response = input("Give 4 numbers 0-9: ").split()
        for x in range(4):
            response[x] = int(response[x])
        result = game.check_response(response)
        # Check if the answer is correct. If correct STOP
        if result:
            print("CORRECT! You found the secret")
            found = True
            break
        # Else, find guesses in correct position, and guesses in wrong position
        feedback = game.get_feedback()
        # Display display all responses and feedbacks
        for i in range(len(game.responses)):
            print(game.responses[i], game.feedbacks[i])

    if not found:
        print("GAME OVER< secret not found")

    ### SAVE THE RESULT IN A CSV FILE:
    ### EXAMPLE:
    ### case of win: username,found,steps (e.g. geogre,found,7)
    ### case of lose: username,lost (e.g. george,lost)


