from tkinter import *


def button_response():
    print("Button is clicked")


window = Tk()
window.title = "HELLO!"

frame = Frame(window)
frame.grid()

label = Label(frame, text="Hello Tkinter")
label.grid(row=0, column=0)

button = Button(frame, text="Click Me", command=button_response)
button.grid(row=1, column=0)

window.mainloop()
