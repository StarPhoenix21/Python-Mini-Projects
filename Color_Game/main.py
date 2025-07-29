import random
import tkinter as tk
from tkinter import messagebox

# Constants
COLOURS = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White']
TIME_LIMIT = 30

# Global state
score = 0
timeleft = TIME_LIMIT

def next_colour():
    global score, timeleft

    if timeleft > 0:
        user_input = entry.get().strip().lower()
        correct_colour = COLOURS[1].lower()  # The colour of the text

        if user_input == correct_colour:
            score += 1

        entry.delete(0, tk.END)
        random.shuffle(COLOURS)
        colour_label.config(fg=COLOURS[1], text=COLOURS[0])
        score_label.config(text=f"Score: {score}")

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        time_label.config(text=f"Time left: {timeleft}")
        time_label.after(1000, countdown)
    else:
        show_high_score()

def save_high_score():
    try:
        with open("highest_score.txt", "r") as f:
            highest = int(f.read())
    except (FileNotFoundError, ValueError):
        highest = 0

    if score > highest:
        with open("highest_score.txt", "w") as f:
            f.write(str(score))

def load_high_score():
    try:
        with open("highest_score.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def show_high_score():
    save_high_score()
    top = tk.Toplevel()
    top.title("High Score")
    top.geometry("250x150")

    msg = f"Your Score: {score}\nHighest Score: {load_high_score()}"
    tk.Label(top, text=msg, font=("Helvetica", 14)).pack(pady=20)
    tk.Button(top, text="Close", command=top.destroy).pack()

def start_game(event):
    global timeleft
    if timeleft == TIME_LIMIT:
        countdown()
    next_colour()

# Setup window
window = tk.Tk()
window.title("Color Game")
window.geometry("375x250")
window.resizable(False, False)

font_name = "Helvetica"

instructions = tk.Label(window, text="Type the COLOR of the text, not the word!", font=(font_name, 12))
instructions.pack(pady=10)

score_label = tk.Label(window, text="Press Enter to start", font=(font_name, 12))
score_label.pack()

time_label = tk.Label(window, text=f"Time left: {timeleft}", font=(font_name, 12))
time_label.pack()

colour_label = tk.Label(window, font=(font_name, 60))
colour_label.pack(pady=20)

entry = tk.Entry(window)
entry.pack()
entry.focus_set()

window.bind('<Return>', start_game)

window.mainloop()
