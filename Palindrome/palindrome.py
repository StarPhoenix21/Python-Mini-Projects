import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    text = entry.get()
    if text == text[::-1]:
        messagebox.showinfo("Result", "It's a palindrome!")
    else:
        messagebox.showinfo("Result", "Not a palindrome.")

# GUI Setup
root = tk.Tk()
root.title("Palindrome Checker")

label = tk.Label(root, text="Enter a string:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check", command=check_palindrome)
check_btn.pack(pady=10)

root.mainloop()
