import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip


def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            raise ValueError("Length must be at least 4")

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = "@#$%&*"

        all_chars = lower + upper + digits + symbols

        password = ''.join(secrets.choice(all_chars) for _ in range(length))
        pyperclip.copy(password)
        messagebox.showinfo("Password Generated", f"Your password:\n\n{password}\n\nCopied to clipboard!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (minimum 4).")

app = tk.Tk()
app.title("🔐 Password Generator")
app.geometry("300x200")
app.resizable(False, False)


tk.Label(app, text="Enter Password Length:", font=("Segoe UI", 11)).pack(pady=10)
length_var = tk.StringVar()
tk.Entry(app, textvariable=length_var, width=20).pack()

tk.Button(app, text="Generate Password", command=generate_password, bg="black", fg="white", padx=10, pady=5).pack(pady=20)

app.mainloop()

