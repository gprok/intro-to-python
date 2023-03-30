import random


class SnakeGame:
    def __init__(self):
        self.lives = 5
        self.body = [
            [200, 200], [200, 210], [200, 220], [200, 230]
        ]
        self.fruit = [0, 0]
        self.direction = "Up"

    def move_body_parts(self):
        for pos in range(len(self.body)-1, 0, -1):
            self.body[pos][0] = self.body[pos-1][0]
            self.body[pos][1] = self.body[pos-1][1]

    def move_up(self):
        if self.direction != "Down":
            self.move_body_parts()
            self.body[0][1] -= 10
            self.direction = "Up"

    def move_down(self):
        if self.direction != "Up":
            self.move_body_parts()
            self.body[0][1] += 10
            self.direction = "Down"

    def move_left(self):
        if self.direction != "Right":
            self.move_body_parts()
            self.body[0][0] -= 10
            self.direction = "Left"

    def move_right(self):
        if self.direction != "Left":
            self.move_body_parts()
            self.body[0][0] += 10
            self.direction = "Right"

    def set_fruit(self):
        x = random.randint(1, 390)
        y = random.randint(1, 390)
        x = x - (x % 10)
        y = y - (y % 10)
        self.fruit = [x, y]

    def increase_body(self):
        x = self.body[-1][0]
        y = self.body[-1][1]
        self.body.append([x, y])

