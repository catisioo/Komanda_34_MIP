import tkinter as tk
from functions import *
# vēl nav gatavs un ir momenti, kurus jārisinā, piemēram kad uzspied uz new game tie random numbers paliek tadi paši, nevis jaunie
def update_current_number_label():
    if current_number:
        current_number_label.config(text=f"Current Number: {current_number}")
    else:
        current_number_label.config(text="Please select a number")

def on_number_button_click(number):
    global current_number
    current_number = number
    update_current_number_label()

def on_divide_button_click(divisor):
    global current_number, p1_points, p2_points, turn, game_over
    if not current_number:
        return
    if current_number % divisor == 0:
        new_number = current_number // divisor
        if new_number % 2 == 0:
            if turn == 1:
                p1_points += 1
            else:
                p2_points += 1
        else:
            if turn == 1:
                p2_points += 1
            else:
                p1_points += 1
        current_number = new_number
        update_current_number_label()
        update_score_labels()
        check_winner()
        if not game_over:
            change_turn()
    else:
        check_winner() 


def update_score_labels():
    p1_points_label.config(text=f"1. spēlētāja punkti: {p1_points}")
    p2_points_label.config(text=f"2. spēlētāja punkti: {p2_points}")

def change_turn():
    global turn
    turn = 2 if turn == 1 else 1

def check_winner():
    global game_over
    if current_number <= 10:
        if p1_points == p2_points:
            winner_label.config(text="It's a tie!")
        elif p1_points > p2_points:
            winner_label.config(text="Player 1 wins!")
        else:
            winner_label.config(text="Player 2 wins!")
        game_over = True
    elif current_number > 10 and current_number % 2 != 0 and current_number % 3 != 0 and current_number % 4 != 0:
        if p1_points == p2_points:
            winner_label.config(text="It's a tie!")
        elif p1_points > p2_points:
            winner_label.config(text="Player 1 wins!")
        else:
            winner_label.config(text="Player 2 wins!")
        game_over = True

def reset_game():
    global current_number, p1_points, p2_points, turn, game_over
    current_number = None
    p1_points = 0
    p2_points = 0
    turn = turn_choice.get()
    game_over = False
    update_current_number_label()
    update_score_labels()
    winner_label.config(text="")

def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About authors")
    label = tk.Label(about_window, text="Iļja Poļivko\nMārtiņš Ņikiforovs\nRaitis Bērtulis\nHaralds Popovs\nDaniela Alise Smelte\nViktors Krasnoborodjko", padx=100, pady=100)
    label.pack()

root = tk.Tk()
root.geometry("900x600")
root.title("1. praktiskais darbs")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Current number label
current_number = None
current_number_label = tk.Label(main_frame, text="Please select a number", font=('Cascadia Mono ExtraLight', 18))
current_number_label.grid(row=0, column=0, columnspan=2)

# Number buttons
numbers_frame = tk.Frame(main_frame)
numbers_frame.grid(row=1, column=0)

for i, number in enumerate(generate_numbers2()):
    button = tk.Button(numbers_frame, text=str(number), font=('Cascadia Mono ExtraLight', 16), command=lambda num=number: on_number_button_click(num))
    button.grid(row=i, column=0, pady=5)

# Divide buttons
divide_frame = tk.Frame(main_frame)
divide_frame.grid(row=1, column=1)

for i, divisor in enumerate([2, 3, 4]):
    button = tk.Button(divide_frame, text=f"/{divisor}", font=('Cascadia Mono ExtraLight', 16), command=lambda div=divisor: on_divide_button_click(div))
    button.grid(row=i, column=0, pady=5)

# Player turn and algorithm selection
selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

turn_choice = tk.IntVar(value=1)
tk.Radiobutton(selection_frame, text="Player 1 starts", variable=turn_choice, value=1).pack(side="left", padx=5)
tk.Radiobutton(selection_frame, text="Player 2 starts", variable=turn_choice, value=2).pack(side="left", padx=5)

algorithm_choice = tk.IntVar(value=1)
tk.Radiobutton(selection_frame, text="Mini-max", variable=algorithm_choice, value=1).pack(side="right", padx=5)
tk.Radiobutton(selection_frame, text="Alfa-beta", variable=algorithm_choice, value=2).pack(side="right", padx=5)

# Winner label
winner_label = tk.Label(root, text="", font=('Cascadia Mono ExtraLight', 12))
winner_label.pack(pady=10)

# New game button
new_game_button = tk.Button(root, text="New Game", font=('Cascadia Mono ExtraLight', 10), command=reset_game)
new_game_button.pack()

# Score labels
p1_points_label = tk.Label(root, text="1. spēlētāja punkti: 0", font=('Cascadia Mono ExtraLight', 10))
p1_points_label.pack()

p2_points_label = tk.Label(root, text="2. spēlētāja punkti: 0", font=('Cascadia Mono ExtraLight', 10))
p2_points_label.pack()

# About authors button
about_authors_button = tk.Button(root, text="About authors", font=('Cascadia Mono ExtraLight', 10), command=open_about)
about_authors_button.pack(pady=10)

root.mainloop()
