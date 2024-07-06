import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("500x500")
        master.resizable(False, False)

        # Background image
        self.background_image = tk.PhotoImage(file="background.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Header frame
        self.header_frame = tk.Frame(master, bg="#333", height=50)
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Password Generator", font=("Arial", 18), fg="#fff", bg="#333")
        self.header_label.pack(pady=10)

        # Main frame
        self.main_frame = tk.Frame(master, bg="grey")
        self.main_frame.pack(fill="both", expand=True)

        # Length label and entry
        self.length_label = tk.Label(self.main_frame, text="Length:", font=("Arial", 14), fg="#333")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self.main_frame, width=20, font=("Arial", 14))
        self.length_entry.pack()

        # Character set options
        self.character_set_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.character_set_frame.pack(pady=10)

        self.uppercase_var = tk.IntVar()
        self.lowercase_var = tk.IntVar()
        self.digits_var = tk.IntVar()
        self.punctuation_var = tk.IntVar()

        self.uppercase_checkbox = tk.Checkbutton(self.character_set_frame, text="Uppercase", variable=self.uppercase_var, font=("Arial", 12), fg="#333")
        self.uppercase_checkbox.pack(side="left")

        self.lowercase_checkbox = tk.Checkbutton(self.character_set_frame, text="Lowercase", variable=self.lowercase_var, font=("Arial", 12), fg="#333")
        self.lowercase_checkbox.pack(side="left")

        self.digits_checkbox = tk.Checkbutton(self.character_set_frame, text="Digits", variable=self.digits_var, font=("Arial", 12), fg="#333")
        self.digits_checkbox.pack(side="left")

        self.punctuation_checkbox = tk.Checkbutton(self.character_set_frame, text="Punctuation", variable=self.punctuation_var, font=("Arial", 12), fg="#333")
        self.punctuation_checkbox.pack(side="left")

        # Generate button
        self.generate_button = tk.Button(self.main_frame, text="Generate Password", command=self.generate_password, font=("Arial", 14), fg="#fff", bg="#333")
        self.generate_button.pack(pady=10)

        # Password label and entry
        self.password_label = tk.Label(self.main_frame, text="Password:", font=("Arial", 14), fg="#333")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.main_frame, width=20, font=("Arial", 14))
        self.password_entry.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        character_set = ""

        if self.uppercase_var.get():
            character_set += string.ascii_uppercase
        if self.lowercase_var.get():
            character_set += string.ascii_lowercase
        if self.digits_var.get():
            character_set += string.digits
        if self.punctuation_var.get():
            character_set += string.punctuation

        if not character_set:
            messagebox.showerror("Error", "Please select at least one character set")
            return

        password = ''.join(random.choice(character_set) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

root = tk.Tk()
my_gui = PasswordGenerator(root)
root.mainloop()
