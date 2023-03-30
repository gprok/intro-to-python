from tkinter import Tk, Canvas

x = 200
y = 200


def key_released(event):
    global x
    global y
    key = event.keysym
    if key == "Up":
        y -= 10
    elif key == "Down":
        y += 10
    elif key == "Right":
        x += 10
    elif key == "Left":
        x -= 10
    canvas.delete("all")
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')


window = Tk()

canvas = Canvas(window, bg='white', width=400, height=400)
canvas.grid(row=0, column=0)
canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')
window.bind('<KeyRelease>', key_released)

window.mainloop()



