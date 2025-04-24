import random
import tkinter as tk
from tkinter import messagebox
import os
import sys

colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White']
score = 0
timeleft = 30

def next_colour():
    global score, timeleft

    if timeleft > 0:
        user_input = e.get().lower()
        correct_color = colours[1].lower()

        if user_input == correct_color:
            score += 1
            feedback_label.config(text="✅ Correct!", fg="green")
        elif user_input != "":
            feedback_label.config(text=f"❌ Wrong! It was: {colours[1]}", fg="red")

        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=colours[1], text=colours[0])
        score_label.config(text=f"Score: {score}")

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text=f"Time left: {timeleft}")
        time_label.after(1000, countdown)
    else:
        scoreshow()

def record_highest_score():
    highest_score = load_highest_score()
    if score > highest_score:
        with open("highest_score.txt", "w") as file:
            file.write(str(score))

def load_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            data = file.read()
            if data:
                return int(data)
            else:
                return 0
    except FileNotFoundError:
        return 0

def scoreshow():
    record_highest_score()
    window2 = tk.Toplevel()
    window2.title("HIGH SCORE")
    window2.geometry("300x200")

    label = tk.Label(window2, text=f"Highest Score: {load_highest_score()}", font=(font, 12))
    label.pack()

    # ✅ Restart button that restarts everything
    def restart():
        window2.destroy()
        window.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)

    restart_btn = tk.Button(window2, text="Play Again", command=restart)
    restart_btn.pack(pady=10)

def start_game(event):
    global timeleft
    if timeleft == 30:
        countdown()
    next_colour()

# --- Main Window ---
window = tk.Tk()
font = 'Helvetica'
window.title("Color Game")
window.geometry("375x300")
window.resizable(False, False)

# ✅ Fix: icon only if exists
icon_path = "color_game_icon.ico"
if os.path.exists(icon_path):
    window.iconbitmap(icon_path)

instructions = tk.Label(window, text="Enter the color of the text, not the word!", font=(font, 12))
instructions.pack(pady=10)

score_label = tk.Label(window, text="Press Enter to start", font=(font, 12))
score_label.pack()

time_label = tk.Label(window, text=f"Time left: {timeleft}", font=(font, 12))
time_label.pack()

label = tk.Label(window, font=(font, 60))
label.pack(pady=20)

e = tk.Entry(window)
window.bind('<Return>', start_game)
e.pack()

# ✅ Inline feedback (replaces popups)
feedback_label = tk.Label(window, text="", font=(font, 10))
feedback_label.pack(pady=5)

e.focus_set()

window.mainloop()
