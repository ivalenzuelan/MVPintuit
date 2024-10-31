import tkinter as tk
from tkinter import simpledialog
import random


board = {3: 22, 5: 8, 11: 26, 20: 29, 17: 4, 19: 7, 27: 1, 21: 9, 32: 30, 99: 78}
questions = {
    "What is a good savings rate as a percentage of your income? (10%, 20%, 50%)": "20%",
    "What is the purpose of an emergency fund? (vacation, unexpected expenses, investment)": "unexpected expenses",
    "If your credit score improves, what happens to loan interest rates? (increase, decrease, stay the same)": "decrease",
    "What should be your first financial priority? (investing, saving for emergencies, buying a car)": "saving for emergencies",
}

# Initialize tkinter window
window = tk.Tk()
window.title("Finance Quest: Snakes & Ladders Edition")

# Initialize player data
players = {"Player 1": 1, "Player 2": 1}
current_player = "Player 1"

# Create the board as a 10x10 grid
board_labels = []
for i in range(10):
    row = []
    for j in range(10):
        label = tk.Label(window, text=str(100 - (i * 10 + j)), borderwidth=2, relief="ridge", width=5, height=2)
        label.grid(row=i, column=j)
        row.append(label)
    board_labels.append(row)

# Helper function to move player on the board
def move_player(player):
    position = players[player]
    row = (100 - position) // 10
    col = (100 - position) % 10
    color = "red" if player == "Player 1" else "blue"
    board_labels[row][col].config(bg=color)

# Roll dice function
def roll_dice():
    global current_player
    dice_roll = random.randint(1, 6)
    result_label.config(text=f"{current_player} rolled a {dice_roll}.")
    ask_question(current_player, dice_roll)

# Function to ask financial questions
def ask_question(player, dice_roll):
    question, answer = random.choice(list(questions.items()))
    user_answer = tk.simpledialog.askstring("Question", question)
    if user_answer and user_answer.lower().strip() == answer.lower():
        players[player] += dice_roll
        result_label.config(text=f"{player} answered correctly! Moving {dice_roll} spaces.")
    else:
        result_label.config(text=f"{player} answered incorrectly. No move.")
    check_position(player)

# Check if player landed on snake or ladder
def check_position(player):
    position = players[player]
    if position in board:
        new_position = board[position]
        if position < new_position:
            result_label.config(text=f"{player} climbed a ladder to {new_position}!")
        else:
            result_label.config(text=f"{player} slid down a snake to {new_position}.")
        players[player] = new_position
    if players[player] >= 100:
        result_label.config(text=f"Congratulations! {player} wins!")
    move_player(player)
    switch_player()

# Switch player turn
def switch_player():
    global current_player
    current_player = "Player 2" if current_player == "Player 1" else "Player 1"

# Set up the interactive roll button and result label
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.grid(row=10, column=0, columnspan=5)
result_label = tk.Label(window, text="Welcome to Finance Quest!")
result_label.grid(row=10, column=5, columnspan=5)

# Run the tkinter event loop
window.mainloop()
