from tkinter import *
import math

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
timer = None
timerRunning = False


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global timerRunning

    window.after_cancel(timer)
    timerRunning = False

    reps = 0
    title_text.config(text="Timer", fg=GREEN)
    done_label.config(text='')
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def button_start_pressed():
    global timerRunning

    if timerRunning:
        return
    start_timer()


def start_timer():
    global reps
    global timerRunning

    timerRunning = True
    reps += 1

    if reps % 2 == 1:
        title_text.config(text="Work", fg=GREEN)
        seconds = WORK_MIN * 60
    elif reps % 8 == 0:
        title_text.config(text="Long Break", fg=RED)
        seconds = LONG_BREAK_MIN * 60
    else:
        title_text.config(text="Break", fg=PINK)
        seconds = SHORT_BREAK_MIN * 60

    #
    #window.iconify()
    # window.wm_attributes("-topmost", True)
    # window.wm_attributes("-topmost", False)
    count_down(seconds)
    window.deiconify()
    #window.withdraw()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timeClock = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=timeClock)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ''
        work_sessions = math.floor(reps / 2)

        for i in range(work_sessions):
            mark += '✔'

        done_label.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(0, 0)


title_text = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"), pady=20)
title_text.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(window, text="Start", highlightthickness=0, command=button_start_pressed, width=7, height=1,
                      font=("Arial", 10), borderwidth=1)
start_button.grid(row=2, column=0)
reset_button = Button(window, text="Reset", highlightthickness=0, command=reset_timer, width=7, height=1,
                      font=("Arial", 10), borderwidth=1)
reset_button.grid(row=2, column=2)


done_label = Label(window, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), pady=10)
done_label.grid(row=3, column=1)

# canvas.pack()

window.mainloop()
