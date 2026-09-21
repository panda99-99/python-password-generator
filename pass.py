import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_slider.get()
    
    # Character pools based on user selection
    character_pool = ""
    if include_letters.get():
        character_pool += string.ascii_letters
    if include_numbers.get():
        character_pool += string.digits
    if include_symbols.get():
        character_pool += string.punctuation
        
    # Validation if nothing is selected
    if not character_pool:
        messagebox.showwarning("Selection Error", "Please select at least one option!")
        return
        
    # Generating the random password
    password = "".join(random.choice(character_pool) for _ in range(length))
    
    # Displaying the password in the entry box
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "Nothing to copy! Generate a password first.")

# Main Window Settings
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("420x450")
root.configure(bg="#1e1e2e") # Modern Dark Theme Background
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="🔑 PASSWORD GENERATOR", font=("Helvetica", 16, "bold"), fg="#cdd6f4", bg="#1e1e2e")
title_label.pack(pady=20)

# Password Display Frame
display_frame = tk.Frame(root, bg="#1e1e2e")
display_frame.pack(pady=10)

password_entry = tk.Entry(display_frame, font=("Consolas", 14), width=22, bd=0, bg="#313244", fg="#a6e3a1", justify="center")
password_entry.pack(side=tk.LEFT, ipady=8, padx=5)

copy_btn = tk.Button(display_frame, text="📋 Copy", font=("Helvetica", 10, "bold"), bg="#89b4fa", fg="#11111b", activebackground="#b4befe", bd=0, command=copy_to_clipboard, padx=10, pady=5)
copy_btn.pack(side=tk.LEFT, padx=5)

# Password Length Controls
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 11), fg="#bac2de", bg="#1e1e2e")
length_label.pack(pady=(15, 2))

length_slider = tk.Scale(root, from_=6, to=32, orient=tk.HORIZONTAL, length=280, bg="#1e1e2e", fg="#cdd6f4", highlightthickness=0, troughcolor="#313244", activebackground="#89b4fa")
length_slider.set(12) # Default value
length_slider.pack()

# Checkboxes Frame
options_frame = tk.LabelFrame(root, text=" Customise Options ", font=("Helvetica", 10, "bold"), fg="#cdd6f4", bg="#1e1e2e", bd=1, relief=tk.SOLID, padx=20, pady=10)
options_frame.pack(pady=25)

include_letters = tk.BooleanVar(value=True)
include_numbers = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Include Letters (a-z, A-Z)", variable=include_letters, font=("Helvetica", 10), bg="#1e1e2e", fg="#cdd6f4", activebackground="#1e1e2e", activeforeground="#a6e3a1", selectcolor="#313244").pack(anchor="w", pady=2)
tk.Checkbutton(options_frame, text="Include Numbers (0-9)", variable=include_numbers, font=("Helvetica", 10), bg="#1e1e2e", fg="#cdd6f4", activebackground="#1e1e2e", activeforeground="#a6e3a1", selectcolor="#313244").pack(anchor="w", pady=2)
tk.Checkbutton(options_frame, text="Include Symbols (@, #, $)", variable=include_symbols, font=("Helvetica", 10), bg="#1e1e2e", fg="#cdd6f4", activebackground="#1e1e2e", activeforeground="#a6e3a1", selectcolor="#313244").pack(anchor="w", pady=2)

# Generate Button
generate_btn = tk.Button(root, text="⚡ Generate Password", font=("Helvetica", 12, "bold"), bg="#a6e3a1", fg="#11111b", activebackground="#94e2d5", bd=0, width=22, pady=8, command=generate_password)
generate_btn.pack(pady=10)

root.mainloop()
