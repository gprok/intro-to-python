from tkinter import Tk, Canvas
from SnakeGame import SnakeGame

# EXERCISE
# 1. Display lives under the canvas
# 2. Don't allow snake to go out of canvas
# 3. If snake head hits the border of canvas, decrease lives and update lives label
# 4. If lives become ZERO, display GAME OVER and stop moving the snake.
# 5. Can you add a PLAY AGAIN button to start over?

game = SnakeGame()


def draw_snake():
    for part in game.body:
        canvas.create_rectangle(part[0], part[1], part[0]+10, part[1]+10, fill='green')


def draw_fruit():
    canvas.create_rectangle(game.fruit[0], game.fruit[1], game.fruit[0] + 10, game.fruit[1] + 10, fill='red')


def eat_fruit():
    head = game.body[0]
    if head[0] == game.fruit[0] and head[1] == game.fruit[1]:
        game.increase_body()
        game.set_fruit()


def key_released(event):
    key = event.keysym
    if key == "Up":
        game.move_up()
    elif key == "Down":
        game.move_down()
    elif key == "Left":
        game.move_left()
    elif key == "Right":
        game.move_right()
    eat_fruit()
    canvas.delete("all")
    draw_snake()
    draw_fruit()


window = Tk()

canvas = Canvas(window, bg='white', width=400, height=400)
canvas.grid(row=0, column=0)
draw_snake()
game.set_fruit()
draw_fruit()
window.bind('<KeyRelease>', key_released)

window.mainloop()



