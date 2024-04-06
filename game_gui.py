import tkinter as tk
#from functions import *
from othermain import *
import time

global gui_number
gui_number = generate_numbers()

global whoStarts
whoStarts = 1

global history
history = []

global history_turn
history_turn = 1

root = tk.Tk()
# gui number    
def gui_numuri():
    global gui_number
    gui_number = generate_numbers()
    print(gui_number)
    return gui_number

def retrieve_current_number():
    number = print_currentNr()
    return number

# Every Turn
def update_current_number(value):
    currentNr = retrieve_current_number()
    currentNrLabel2.config(text = currentNr)
    return currentNr

# New Game
def update_all_numbers(gui_number):
    
    #dividerLabel.config(text="")
    currentNrLabel2.config(text="")
    
    num1button.config(text=gui_number[0])
    num2button.config(text=gui_number[1])
    num3button.config(text=gui_number[2])
    num4button.config(text=gui_number[3])
    num5button.config(text=gui_number[4])

# executes after every turn
def game_tick(value):
    game_status = check_game_status()
    divisor = value
    global whoStarts
    
    if game_status == 1:
        turn = whoStarts
        
        if turn == 1:
            currentNR = update_current_number(value)
            if currentNR % 2 != 0 and currentNR % 3 != 0 and currentNR % 4 != 0:
                print("Spele Beigusies")
                game_end()
                return "Spēle beigusies!"
            
            if currentNR % divisor != 0:
                print("Invalid Divider")
                return "Invalid Divider"
            
            invalid = man_vs_machine(turn,divisor)
            update_devider_label(divisor)
            update_score()
            
            if invalid == 1:
                return "Invalid Divider"
            
            update_turn_history(currentNR,divisor)
            
            whoStarts = 2
            #time.sleep(1)
            currentNR = update_current_number(value)
            AI_turn()
            AI_devider = get_devider()
            update_devider_label(AI_devider)
            update_score()
            #update_turn_history(currentNR,AI_devider)
            currentNR = update_current_number(value)
            if currentNR % 2 != 0 and currentNR % 3 != 0 and currentNR % 4 != 0:
                game_end()
                print("Spele Beigusies")
                return "Spēle beigusies!"
            update_turn_history(currentNR,AI_devider)
        else:
            AI_turn()
            AI_devider = get_devider()
            currentNR = update_current_number(value)
            update_turn_history(currentNR,AI_devider)
            update_devider_label(AI_devider)
            update_score()
    
    else:
        print("Game not started!")

def AI_turn():
    global whoStarts
    divisor = 2
    man_vs_machine(whoStarts,divisor)
    update_current_number(divisor)
    whoStarts = 1

def number_selection(currentNumber):
    chose_number(currentNumber)
    update_current_number(currentNumber)
    return None

root.geometry("900x600")
root.title("1. praktiskais darbs")

currentNrLabel = tk.Label(root, text = "Current Number:", font = ('Cascadia Mono ExtraLight', 18))
currentNrLabel.pack(padx = 20, pady = 40)

currentNrLabel2 = tk.Label(root, text='', font = ('Cascadia Mono ExtraLight', 18))
currentNrLabel2.pack(padx = 20, pady = 40)

#dividerLabel = tk.Label(root, text='', font = ('Cascadia Mono ExtraLight', 18))
#dividerLabel.pack(padx = 0, pady = 0)

#resultLabel = tk.Label(root, text='', font= ('Cascadia Mono ExtraLight', 18))
#resultLabel.pack(padx = 0, pady = 0 )

turn_history_label = tk.Label(root, text="Turn History", font=('Cascadia Mono ExtraLight', 16))
turn_history_label.pack(padx = 20, pady = 0)

resultListBox = tk.Listbox(root)
resultListBox.pack()

def update_devider_label(value):
    divider = '/' + str(value)
    #dividerLabel.config(text=divider)
    
def update_result_label(result):
    return None
    #dividerLabel.config(text=result)

# Piedāvāju šādu variantu (iekomentētā daļa):

leftFrame = tk.Frame(root)
leftFrame.place(x=50, y=150, width=200, height=400)

num1button = tk.Button(leftFrame, text=gui_number[0], font=('Cascadia Mono ExtraLight', 16), command=lambda: number_selection(gui_number[0]))
num1button.pack(padx=20, pady=10)

num2button = tk.Button(leftFrame, text=gui_number[1], font=('Cascadia Mono ExtraLight', 16), command=lambda: number_selection(gui_number[1]))
num2button.pack(padx=20, pady=10)

num3button = tk.Button(leftFrame, text=gui_number[2], font=('Cascadia Mono ExtraLight', 16), command=lambda: number_selection( gui_number[2]))
num3button.pack(padx=20, pady=10)

num4button = tk.Button(leftFrame, text=gui_number[3], font=('Cascadia Mono ExtraLight', 16),command=lambda: number_selection(gui_number[3]))
num4button.pack(padx=20, pady=10)

num5button = tk.Button(leftFrame, text=gui_number[4], font=('Cascadia Mono ExtraLight', 16),command=lambda: number_selection(gui_number[4]))
num5button.pack(padx=20, pady=10)

rightFrame = tk.Frame(root)
rightFrame.place(x=600, y=200, width=200, height=300)

div2button = tk.Button(rightFrame, text="/2", font=('Cascadia Mono ExtraLight', 16), command=lambda: game_tick(2))
div2button.pack(padx=20, pady=20)

div3button = tk.Button(rightFrame, text="/3", font=('Cascadia Mono ExtraLight', 16), command=lambda: game_tick(3))
div3button.pack(padx=20, pady=0)

div4button = tk.Button(rightFrame, text="/4", font=('Cascadia Mono ExtraLight', 16), command=lambda: game_tick(4))
div4button.pack(padx=20, pady=20)

def radiobutton_izvele():
    global whoStarts
    if izveles_vertiba.get() == 1:
        izvades_teksts.set(f"Izvēlēts 1. spēlētājs")
        whoStarts = 1
        who_starts(whoStarts = 1)
    else:
        izvades_teksts.set(f"Izvēlēts 2. spēlētājs")
        whoStarts = 2
        who_starts(whoStarts = 2)

izveles_vertiba = tk.IntVar()
izvades_teksts = tk.StringVar()
izveles_vertiba2 = tk.IntVar()
izvades_teksts2 = tk.StringVar()

radio1Frame = tk.Frame(root)
radio1Frame.place(x=55, y=40, width=200, height=75)

radio1label = tk.Label(radio1Frame, text = "Kurš spēlētājs sāks spēli?", font = ('Cascadia Mono ExtraLight', 8))
radio1label.pack()

rb1 = tk.Radiobutton(radio1Frame, text="Spēlētājs", font=('Cascadia Mono ExtraLight', 8), variable=izveles_vertiba, value=1, command=radiobutton_izvele)
rb1.pack()

rb2 = tk.Radiobutton(radio1Frame, text="Dators", font=('Cascadia Mono ExtraLight', 8), variable=izveles_vertiba, value=2, command=radiobutton_izvele)
rb2.pack()

def radiobutton_izvele2():
    if izveles_vertiba2.get() == 1:
        izvades_teksts2.set(f"Izvēlēts Mini-max algoritms")
        algorithm(whichAlgorithm = 1)
    else:
        izvades_teksts2.set(f"Izvēlēts Alfa-beta algoritms")
        algorithm(whichAlgorithm = 2) 

radio2Frame = tk.Frame(root)
radio2Frame.place(x=600, y=40, width=200, height=75)

radio2label = tk.Label(radio2Frame, text = "Izvēlies algoritmu:", font = ('Cascadia Mono ExtraLight', 8))
radio2label.pack()

rb3 = tk.Radiobutton(radio2Frame, text="Mini-max", font=('Cascadia Mono ExtraLight', 8), variable=izveles_vertiba2, value=1, command=radiobutton_izvele2)
rb3.pack()

rb4 = tk.Radiobutton(radio2Frame, text="Alfa-beta", font=('Cascadia Mono ExtraLight', 8), variable=izveles_vertiba2, value=2, command=radiobutton_izvele2)
rb4.pack()

speletaja_label = tk.Label(root, textvariable=izvades_teksts, font=('Cascadia Mono ExtraLight', 10))
speletaja_label.place(x=65, y=120)

algoritma_label = tk.Label(root, textvariable=izvades_teksts2, font=('Cascadia Mono ExtraLight', 10))
algoritma_label.place(x=580, y=120)

newGameFrame = tk.Frame(root)
newGameFrame.place(x=760, y=520)

def new_game():
    guiNr = gui_numuri()
    print(guiNr)
    update_all_numbers(guiNr)
    is_game_runing = 0
    update_game_status(is_game_runing)
    
    global whoStarts
    whoStarts = 1
    
    global history_turn
    update_score()
    lenght = len(history)    
    print(history)
    i = 0
    
    while i  <= history_turn:
        resultListBox.delete(0)
        i=1+i
    
    history_turn = 1    

def start_game():
    is_game_runing = 1
    prepare_start()
    update_game_status(is_game_runing)
    currentNR = update_current_number(1)
    
    global whoStarts
    update_score()
    #open_game_table()
    
    if whoStarts == 2:
        AI_turn()
        AI_devider = get_devider()
        update_devider_label(AI_devider)
        update_score()
        update_turn_history(currentNR,AI_devider)

def game_end():
    is_game_runing = 0
    open_game_over()
    return "Spele Beigusies"

startGameButton = tk.Button((newGameFrame), text="Start Game", font=('Cascadia Mono ExtraLight', 10), command = start_game)
startGameButton.pack(padx=0, pady=0)

newGamebutton = tk.Button(newGameFrame, text="New Game", font=('Cascadia Mono ExtraLight', 10), command=new_game)
newGamebutton.pack(padx=0, pady=0)

punktuFrame = tk.Frame(root)
punktuFrame.place(x=360, y=520)

def update_score():
    score = get_points()
    print(score)
    
    player_Score = "Spēlētāja punkti: "+ str(score[0])
    AI_Score = "   Datora punkti: " + str(score[1])
    
    punkti1label.config(text=player_Score)
    punkti2label.config(text=AI_Score)
    return score
    
punkti1label = tk.Label(punktuFrame, text = "Spēlētāja punkti: 0", font = ('Cascadia Mono ExtraLight', 10),relief="sunken")
punkti1label.pack()

punkti2label = tk.Label(punktuFrame, text = "   Datora punkti: 0", font = ('Cascadia Mono ExtraLight', 10),relief="sunken")
punkti2label.pack()

def update_turn_history(number,divider):
    result = number / divider
    global history_turn
    history_entry = str(number)+ " /" +str(divider)+" = "+ str(result) 
    resultListBox.insert(history_turn,history_entry)
    history_turn = history_turn + 1
    history.append(history_entry)

def open_game_over():
    game_end_window = tk.Toplevel(root)
    game_end_window.title("Game Over!")
    score = get_points()
    
    if score[0] == score[1]:
        uzvaretajs = tk.Label(game_end_window,text="Neizšķirts!")
        uzvaretajs.pack()
    
    if score[0] > score[1]:
        uzvaretajs = tk.Label(game_end_window,text="Tu uzvarēji!")
        uzvaretajs.pack()
    
    if score[0] < score[1]:
        uzvaretajs = tk.Label(game_end_window,text="Tu zaudēji!")       
        uzvaretajs.pack()

def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About authors")
    label = tk.Label(about_window, text="Iļja Poļivko\nMārtiņš Ņikiforovs\nRaitis Bērtulis\nHaralds Popovs\nDaniela Alise Smelte\nViktors Krasnoborodjko", padx = 100, pady = 100)
    label.pack()

about_authors = tk.Button(root, text = "About authors", font = ('Cascadia Mono ExtraLight', 10), command=open_about)
about_authors.place(relx=1, x=-5, y=5, anchor="ne")

root.mainloop()