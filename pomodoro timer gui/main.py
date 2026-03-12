import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_stop = None
break_stop = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global work_stop , break_stop
    if work_stop is not None:
        window.after_cancel(work_stop)
        work_stop = None
    if break_stop is not None:
        window.after_cancel(break_stop)
        break_stop = None
    timer_label.config(text="Timer")
    reps = 0
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text= "00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def holder():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in [1, 3, 5, 7]:
        timer_label.config(text="Work", fg=RED)
        work_timer(work_sec)
    elif reps == 8:
        timer_label.config(text="Long Break", fg=GREEN)
        break_timer(long_break_sec)

    else:
        timer_label.config(text="Break", fg=PINK)
        break_timer(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def work_timer(count):

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        global work_stop
        work_stop =  window.after(1000,work_timer, count-1)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    else:
        if reps <8:
            holder()
            mark = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                mark+="✔"
            check_mark.config(text=mark)

def break_timer(count):

    count_min = math.floor(count/60)
    count_sec = math.floor(count % 60)
    if count_sec <10:
        count_sec = f"0{count_sec}"
    if count > 0:
        global break_stop
        break_stop = window.after(1000, break_timer, count-1)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    else:
        if reps < 8:  # only continue if not finished
            holder()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Podoromo")
window.config(padx=100,pady=150,bg=YELLOW)
window.wm_minsize(width=500, height=500)

# tomato png input
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# buttons and labels and check mark

start_button= Button(text="Start",highlightthickness=0,command=holder)
start_button.place(x=0, y=270)
reset_button= Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.place(x=250, y=270)

timer_label = Label(text="Timer",bg=YELLOW,font=(FONT_NAME,45,"bold"), fg=GREEN )
timer_label.place(x=60,y=-75)

check_mark = Label(bg=YELLOW,fg=GREEN)
check_mark.place(x=100,y=275)

window.mainloop()