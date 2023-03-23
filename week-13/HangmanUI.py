from HangmanModel import HangmanModel
from tkinter import Tk, Label, Text, Button, END, Canvas


def play():
    letter = field.get("1.0")
    model.play(letter)
    field.delete("1.0", END)
    secret_label.configure(text=model.get_secret())
    draw_hangman()
    if model.found():
        message.configure(text="Congrats! Word found!")
        play_btn["state"] = "disabled"
    if model.hanged():
        message.configure(text="You are hanged ...")
        play_btn["state"] = "disabled"


def play_again():
    model.start()
    secret_label.configure(text=model.get_secret())
    play_btn["state"] = "normal"
    message.configure(text='')
    canvas.delete("all")


def draw_hangman():
    wrong = len(model.wrong)
    if wrong >= 1:
        canvas.create_oval(120, 120, 160, 160)
    if wrong >= 2:
        canvas.create_line(140, 160, 140, 220)
    if wrong >= 3:
        canvas.create_line(140, 220, 100, 260)
    if wrong >= 4:
        canvas.create_line(140, 220, 180, 260)
    if wrong >= 5:
        canvas.create_line(140, 190, 100, 160)
    if wrong >= 6:
        canvas.create_line(140, 190, 180, 160)


window = Tk()
model = HangmanModel()
model.start()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)


secret_label = Label(window, text=model.get_secret())
secret_label.grid(row=1, column=0)

field = Text(window, width=5, height=1)
field.grid(row=2, column=0)

play_btn = Button(window, text="Play", command=play)
play_btn.grid(row=3, column=0)

message = Label(window, text='')
message.grid(row=4, column=0)

play_again_btn = Button(window, text='Play Again', command=play_again)
play_again_btn.grid(row=5, column=0)

window.mainloop()

