import math
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
TICK_MARK = "✔"
reps = 0
timer = None

def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    tick_mark.config(text="")


def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work Time", fg=GREEN)


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text,  text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += TICK_MARK
        tick_mark.config(text=marks)




window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(height=224, width=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(112, 112, image=tomato_img)

timer_text = canvas.create_text(112, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

tick_mark = Label(fg=GREEN, bg=YELLOW)
tick_mark.grid(row=3, column=1)

window.mainloop()