import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.geometry("500x400")
        master.resizable(False, False)

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Header frame
        self.header_frame = tk.Frame(master, bg="#333", height=50)
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Rock Paper Scissors", font=("Arial", 24, "bold"), fg="#fff", bg="#333")
        self.header_label.pack(pady=10)

        # Main frame
        self.main_frame = tk.Frame(master, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True)

        # Player choice frame
        self.player_choice_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.player_choice_frame.pack(pady=20)

        self.choice_label = tk.Label(self.player_choice_frame, text="Choose your move:", font=("Arial", 18), fg="#333")
        self.choice_label.pack()

        self.rock_button = tk.Button(self.player_choice_frame, text="Rock", command=lambda: self.play("rock"), font=("Arial", 18), fg="#fff", bg="#333", width=10)
        self.rock_button.pack(side="left", padx=10)

        self.paper_button = tk.Button(self.player_choice_frame, text="Paper", command=lambda: self.play("paper"), font=("Arial", 18), fg="#fff", bg="#333", width=10)
        self.paper_button.pack(side="left", padx=10)

        self.scissors_button = tk.Button(self.player_choice_frame, text="Scissors", command=lambda: self.play("scissors"), font=("Arial", 18), fg="#fff", bg="#333", width=10)
        self.scissors_button.pack(side="left", padx=10)

        # Score frame
        self.score_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.score_frame.pack(pady=20)

        self.score_label = tk.Label(self.score_frame, text="Score:", font=("Arial", 18), fg="#333")
        self.score_label.pack()

        self.user_score_label = tk.Label(self.score_frame, text=f"User: {self.user_score}", font=("Arial", 18), fg="#333")
        self.user_score_label.pack()

        self.computer_score_label = tk.Label(self.score_frame, text=f"Computer: {self.computer_score}", font=("Arial", 18), fg="#333")
        self.computer_score_label.pack()

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        messagebox.showinfo("Result", f"User: {user_choice}, Computer: {computer_choice}\n{result}")

        self.user_score_label.config(text=f"User: {self.user_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")

root = tk.Tk()
my_game = RockPaperScissors(root)
root.mainloop()
