from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Take A Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Take A Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.config(fg="blue", highlightthickness=0)
start_button.grid(column=0, row=2)

check_mark_label = Label(text="✔️")
check_mark_label.config(bg=YELLOW, highlightthickness=0, fg=GREEN)
check_mark_label.grid(column=1,row=3)

reset_button = Button(text="Reset")
reset_button.config(fg="blue", highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
