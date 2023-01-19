from tkinter import *
import time

GREEN = "#9bdeac"

window = Tk()
window.title('How Fast Do you Type?')
window.geometry('750x464')
T = Text(window)
T.grid(row=0, columnspan=2)
then = time.time()
canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
counter = canvas.create_text(100, 130, text="0 words per minute")
canvas.grid(row=0, column=2, columnspan=1)


def calculate_text(e):
    text = T.get('1.0', 'end-1c')
    words = len(text.split())
    words_per_minute = (words * 60) // int(time.time() - then)
    # print(words_per_minute)
    canvas.itemconfig(counter, text=f"{words_per_minute} words per minute")


window.bind('<space>', calculate_text)
window.mainloop()
