import math
from tkinter import *
import time
reps = 0
timer = None

# Reseting timer
def reset_timer():
    window.after_cancel(timer)
    top_text.config(text='Timer', fg='green')
    canvas.itemconfig(timer_text, text='00:00')
    check_label.config(text='')
    global reps
    reps = 0





# Setting timer
def start_timer():
    global reps
    reps += 1
    work_min = 25
    short_break_min = 5
    long_break_min = 20
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        top_text.config(text='Break', fg='green')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_text.config(text='Break', fg='pink')
    else:
        count_down(work_sec)
        top_text.config(text='Work', fg='red')

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checks = ''
        work_reps = math.floor(reps/2)
        for _ in range(work_reps):
            checks += '✅'
        check_label.config(text=checks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224)
image = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=('Arial Black', 35, 'bold'))
canvas.grid(column=2, row=2)

top_text = Label(text='Timer', fg='#9bdeac', font=('Arial Black', 20, 'bold'))
top_text.grid(column=2, row=1)

start_btn = Button(text='Start', command=start_timer)
start_btn.grid(column=1, row=3)

reset_btn = Button(text='Reset', command=reset_timer)
reset_btn.grid(column=3, row=3)

check_label = Label(text='', fg='green')
check_label.grid(column=2, row=4)

window.mainloop()