import random
import tkinter as tk
from tkinter import messagebox

# A list of colors to be used in the game.
colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White']
score = 0
timeleft = 30
game_started = False
current_fg_color = ""

def load_highest_score():
    """Loads the highest score from a text file, returns 0 if the file doesn't exist."""
    try:
        with open("highest_score.txt", "r") as file:
            data = file.read()
            return int(data) if data else 0
    except FileNotFoundError:
        return 0

def record_highest_score():
    """Checks if the current score is a new high score and saves it to a file."""
    highest_score = load_highest_score()
    if score > highest_score:
        with open("highest_score.txt", "w") as file:
            file.write(str(score))
    return load_highest_score()

def next_colour():
    """Updates the game state, checks the user's input, and changes the displayed color word."""
    global score, current_fg_color

    if timeleft > 0:
        user_input = e.get().lower()

        # Check if the user's input matches the *actual* color of the text.
        # This fixes the original bug where the check was unreliable after shuffling.
        if user_input == current_fg_color.lower():
            score += 1

        e.delete(0, tk.END)
        random.shuffle(colours)

        # Update the label with a new word and a new text color.
        label.config(fg=colours[1], text=colours[0])
        current_fg_color = colours[1]
        score_label.config(text=f"Score: {score}")

def countdown():
    """Manages the game timer and triggers the game over state when time runs out."""
    global timeleft, game_started

    if timeleft > 0 and game_started:
        timeleft -= 1
        time_label.config(text=f"Time left: {timeleft}")
        time_label.after(1000, countdown)
    elif game_started:
        game_started = False
        highest_score = record_highest_score()
        # Use a messagebox instead of a separate window for a better user experience.
        messagebox.showinfo('Game Over', f'Time is out! Your score is {score}.\nYour highest score is {highest_score}.')
        reset_game()

def reset_game():
    """Resets all game variables and UI elements for a new game."""
    global score, timeleft, game_started
    score = 0
    timeleft = 30
    game_started = False
    score_label.config(text=f"Score: {score}")
    time_label.config(text=f"Time left: {timeleft}")
    highest_score_label.config(text=f"Highest Score: {load_highest_score()}")
    label.config(text="Press Enter to start", fg="black")
    e.focus_set()

def start_game(event):
    """Starts the game and the timer on the first key press."""
    global game_started
    if not game_started:
        game_started = True
        countdown()
    next_colour()

# Main window setup
window = tk.Tk()
font = 'Helvetica'
window.title("Color Game")
# Note: The icon file "color_game_icon.ico" is not included, so this line is commented out.
# window.iconbitmap("color_game_icon.ico")
window.geometry("375x250")
window.resizable(False, False)

# UI elements
instructions = tk.Label(window, text="Enter the color of the text, not the word!", font=(font, 12))
instructions.pack(pady=10)

highest_score_label = tk.Label(window, text=f"Highest Score: {load_highest_score()}", font=(font, 12))
highest_score_label.pack()

score_label = tk.Label(window, text="Press Enter to start", font=(font, 12))
score_label.pack()
 
time_label = tk.Label(window, text=f"Time left: {timeleft}", font=(font, 12))
time_label.pack()

label = tk.Label(window, font=(font, 60))
label.pack(pady=20)

e = tk.Entry(window)
window.bind('<Return>', start_game)
e.pack()

e.focus_set()

window.mainloop()
p()
