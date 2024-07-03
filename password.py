import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(entry.get())
    characters = ""
    if var_characters.get():
        characters += string.ascii_letters
    if var_numbers.get():
        characters += string.digits
    if var_punctuation.get():
        characters += string.punctuation
    
    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    else:
        result_label.config(text="Select at least one option")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
    messagebox.showinfo("Password Generator", "Password copied to clipboard")

# Main window
root = tk.Tk()
root.title("Password Generator")

# Create UI elements
frame = tk.Frame(root)
frame.pack(padx=200, pady=200)

label = tk.Label(frame, text="Enter the length of the password:")
label.pack(pady=10)

entry = tk.Entry(frame)
entry.pack(pady=5)

# Checkboxes for complexity
var_characters = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_punctuation = tk.BooleanVar()

check_characters = tk.Checkbutton(frame, text="Characters", variable=var_characters)
check_characters.pack(pady=5)

check_numbers = tk.Checkbutton(frame, text="Numbers", variable=var_numbers)
check_numbers.pack(pady=5)

check_punctuation = tk.Checkbutton(frame, text="Punctuation", variable=var_punctuation)
check_punctuation.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Helvetica", 12))
result_label.pack(pady=5)

# Run the application
root.mainloop()
