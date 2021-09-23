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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    # reset the timer
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    # Count down
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="20 minutes breaj", bg=YELLOW, fg=PINK)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        label_timer.config(text="5 minutes break", bg=YELLOW, fg=RED)
    else:
        count_down(work_sec)
        label_timer.config(text="Work Work Work", bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    minute = math.floor(count/60)
    second = count % 60
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")


# Labels
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_timer.grid(row=0, column=1)

# Start Buttons
button_start = Button(bg=YELLOW, text="Start", command=start_timer)
button_start.grid(row=2, column=0)

# Reset Button
button_reset = Button(bg=YELLOW, text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

# Chekmarks
check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)


window.mainloop()