from tkinter import Tk, Canvas


window = Tk()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)

canvas.create_line(10, 10, 10, 100)
canvas.create_rectangle(30, 30, 100, 80, fill="red")

canvas.create_oval(120, 120, 160, 160)
canvas.create_line(140, 160, 140, 220)
canvas.create_line(140, 220, 100, 260)
canvas.create_line(140, 220, 180, 260)
canvas.create_line(140, 190, 100, 160)
canvas.create_line(140, 190, 180, 160)

window.mainloop()
