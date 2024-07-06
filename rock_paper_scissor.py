import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.geometry("400x300")
        master.resizable(False, False)

        # Header frame
        self.header_frame = tk.Frame(master, bg="#333", height=50)
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Rock Paper Scissors", font=("Arial", 18), fg="#fff", bg="#333")
        self.header_label.pack(pady=10)

        # Main frame
        self.main_frame = tk.Frame(master, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True)

        # Player choice frame
        self.player_choice_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.player_choice_frame.pack(pady=10)

        self.rock_button = tk.Button(self.player_choice_frame, text="Rock", command=lambda: self.play("rock"), font=("Arial", 14), fg="#fff", bg="#333")
        self.rock_button.pack(side="left", padx=10)

        self.paper_button = tk.Button(self.player_choice_frame, text="Paper", command=lambda: self.play("paper"), font=("Arial", 14), fg="#fff", bg="#333")
        self.paper_button.pack(side="left", padx=10)

        self.scissors_button = tk.Button(self.player_choice_frame, text="Scissors", command=lambda: self.play("scissors"), font=("Arial", 14), fg="#fff", bg="#333")
        self.scissors_button.pack(side="left", padx=10)

        # Score frame
        self.score_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.score_frame.pack(pady=10)

        self.user_score_label = tk.Label(self.score_frame, text="User Score: 0", font=("Arial", 14), fg="#333")
        self.user_score_label.pack(side="left", padx=10)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Arial", 14), fg="#333")
        self.computer_score_label.pack(side="left", padx=10)

        # Result frame
        self.result_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 14), fg="#333")
        self.result_label.pack()

        # Initialize score
        self.user_score = 0
        self.computer_score = 0

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win this round!"
            self.user_score += 1
        else:
            result = "Computer wins this round!"
            self.computer_score += 1

        self.result_label.config(text=f"Computer chose {computer_choice}. {result}")
        self.user_score_label.config(text=f"User Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

root = tk.Tk()
my_gui = RockPaperScissors(root)
root.mainloop()
