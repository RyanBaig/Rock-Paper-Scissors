import random
import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk, messagebox

options = {
    0: "rock",
    1: "paper",
    2: "scissors"
}


# Functions
def disable():
    rock_.config(state=tk.DISABLED)
    paper_.config(state=tk.DISABLED)
    scissors_.config(state=tk.DISABLED)


def enable():
    rock_.config(state=tk.NORMAL)
    paper_.config(state=tk.NORMAL)
    scissors_.config(state=tk.NORMAL)


def user_choice(choice):
    global user_wins
    global ai_wins
    disable()

    user_choice_label.config(text=f"You Selected: {choice.capitalize()}")
    user_choice_label.pack()

    ai_pick()
    ai_choice_label.config(text=f"AI Selected: {ai_choice}")
    ai_choice_label.pack()

    if ai_choice == choice:
        messagebox.showinfo("Winner", "Its a Tie!")
        enable()
    elif (
            (ai_choice == "rock" and choice == "scissors") or
            (ai_choice == "paper" and choice == "rock") or
            (ai_choice == "scissors" and choice == "paper")
    ):
        messagebox.showinfo("Winner", "You Lose!")
        ai_wins += 1
        enable()
    else:
        messagebox.showinfo("Winner", "You Win!")
        user_wins += 1
        enable()
    score_label.config(text=f"User: {user_wins}  AI: {ai_wins}")
    score_label.pack()


def ai_pick():
    global ai_choice
    ai_choice = random.choice(list(options.values()))


# Create the main window
win = tk.Tk()
win.geometry("400x400")
win.title("Rock Paper Scissors")

win.style = Style(theme="darkly")

# Create a Notebook widget
notebook = ttk.Notebook(win, width=350, height=550)
notebook.pack(pady=20)

# Create tabs for different content
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Game")
notebook.add(tab2, text="Scores")


# Bind the notebook to a function
def on_tab_change(event):
    if notebook.index("current") == 1:  # If "Scores" tab is selected
        user_score_label.config(text=f"User Wins: {user_wins}")
        user_score_label.pack()
        ai_score_label.config(text=f"AI Wins: {ai_wins}")
        ai_score_label.pack()


notebook.bind("<<NotebookTabChanged>>", on_tab_change)

# Create UI elements for the "Game" tab
title = tk.Label(tab1, text="Rock Paper Scissors by Ryan", font=('Helvetica', 16))
title.pack()

button_frame = tk.Frame(tab1)
button_frame.pack()

rock_ = tk.Button(button_frame, text="🪨 Rock", command=lambda: user_choice("rock"))
rock_.pack(side=tk.LEFT, padx=10, pady=10)

paper_ = tk.Button(button_frame, text="📜 Paper", command=lambda: user_choice("paper"))
paper_.pack(side=tk.LEFT, padx=10, pady=10)

scissors_ = tk.Button(button_frame, text="✂️ Scissors", command=lambda: user_choice("scissors"))
scissors_.pack(side=tk.LEFT, padx=10, pady=10)

user_choice_label = tk.Label(tab1, text="", font=('Helvetica', 12))
ai_choice_label = tk.Label(tab1, text="", font=('Helvetica', 12))
result_label = tk.Label(tab1, text="", font=('Helvetica', 16))
score_label = tk.Label(tab1, text="", font=('Helvetica', 16))

# Create UI elements for the "Scores" tab
user_score_label = tk.Label(tab2, text="", font=('Helvetica', 16))
ai_score_label = tk.Label(tab2, text="", font=('Helvetica', 16))

# Initialize game variables
ai_choice = ""
ai_wins = 0
user_wins = 0

# Start the main loop
win.mainloop()
