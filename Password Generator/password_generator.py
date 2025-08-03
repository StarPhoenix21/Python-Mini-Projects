import random
import tkinter as tk
from tkinter import messagebox
import string
import pyperclip

# --- GUI Setup ---
app = tk.Tk()
app.title('Password Generator')
app.geometry('250x200')
app.resizable(False, False)

# --- Functions ---
def generate_password():
    """
    Generates a random password based on the user-specified length.
    It includes letters, numbers, and punctuation symbols.
    """
    try:
        # Get the desired password length from the entry box
        length = int(string_pass.get())

        # Validate that the length is a positive integer
        if length <= 0:
            messagebox.showerror('Invalid Length', 'Please enter a positive number for the password length.')
            return

        # Use the string module for a clean way to define character sets
        all_characters = string.ascii_letters + string.digits + string.punctuation

        # Use random.sample to create a password with the specified length
        # This ensures all characters are unique within the password
        if length > len(all_characters):
            # If the requested length is greater than the available unique characters,
            # use random.choice to allow for repeated characters.
            password = "".join(random.choice(all_characters) for _ in range(length))
        else:
            password = "".join(random.sample(all_characters, length))

        # Display the generated password to the user
        messagebox.showinfo(
            'Password Generated',
            f'Your new password is:\n\n{password}\n\nIt has been copied to your clipboard.'
        )

        # Copy the password to the clipboard
        pyperclip.copy(password)

    except ValueError:
        # Handle cases where the user enters non-integer input
        messagebox.showerror('Invalid Input', 'Please enter a valid number for the password length.')

# --- UI Elements ---
string_pass = tk.StringVar()

label = tk.Label(app, text="Password Length")
label.pack(pady=10)

txt = tk.Entry(app, textvariable=string_pass)
txt.pack()

btn = tk.Button(app, text="Generate", command=generate_password)
btn.pack(pady=10)

# Start the main event loop
app.mainloop()
