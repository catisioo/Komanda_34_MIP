import tkinter as tk
from functions import *
from othermain import *

gui_number = generate_numbers()

root = tk.Tk()

def gui_numuri():
    gui_number = generate_numbers()
    print(gui_number)

root.geometry("900x600")
root.title("1. praktiskais darbs")

currentNrLabel = tk.Label(root, text = "Current Number:", font = ('Cascadia Mono ExtraLight', 18))
currentNrLabel.pack(padx = 20, pady = 40)

# Piedāvāju šādu variantu (iekomentētā daļa):

leftFrame = tk.Frame(root)
leftFrame.place(x=50, y=150, width=200, height=400)

num1button = tk.Button(leftFrame, text=gui_number[0], font=('Cascadia Mono ExtraLight', 16),command=lambda: chose_number(gui_number[0]))
num1button.pack(padx=20, pady=10)

num2button = tk.Button(leftFrame, text=gui_number[1], font=('Cascadia Mono ExtraLight', 16),command=lambda: chose_number(gui_number[1]))
num2button.pack(padx=20, pady=10)

num3button = tk.Button(leftFrame, text=gui_number[2], font=('Cascadia Mono ExtraLight', 16),command=lambda: chose_number(gui_number[2]))
num3button.pack(padx=20, pady=10)

num4button = tk.Button(leftFrame, text=gui_number[3], font=('Cascadia Mono ExtraLight', 16),command=lambda: chose_number(gui_number[3]))
num4button.pack(padx=20, pady=10)

num5button = tk.Button(leftFrame, text=gui_number[4], font=('Cascadia Mono ExtraLight', 16),command=lambda: chose_number(gui_number[4]))
num5button.pack(padx=20, pady=10)

rightFrame = tk.Frame(root)
rightFrame.place(x=600, y=200, width=200, height=300)

div2button = tk.Button(rightFrame, text="/2", font=('Cascadia Mono ExtraLight', 16))
div2button.pack(padx=20, pady=20)

div3button = tk.Button(rightFrame, text="/3", font=('Cascadia Mono ExtraLight', 16))
div3button.pack(padx=20, pady=0)

div4button = tk.Button(rightFrame, text="/4", font=('Cascadia Mono ExtraLight', 16))
div4button.pack(padx=20, pady=20)

def radiobutton_izvele():
    if izveles_vertiba.get() == 1:
        izvades_teksts.set(f"Izvēlēts 1. spēlētājs")
    else:
        izvades_teksts.set(f"Izvēlēts 2. spēlētājs")                                                    

izveles_vertiba = tk.IntVar()
izvades_teksts = tk.StringVar()
izveles_vertiba2 = tk.IntVar()
izvades_teksts2 = tk.StringVar()

radio1Frame = tk.Frame(root)
radio1Frame.place(x=55, y=40, width=200, height=75)

radio1label = tk.Label(radio1Frame, text = "Izvēlies spēlētāju:", font = ('Cascadia Mono ExtraLight', 8))
radio1label.pack()

rb1 = tk.Radiobutton(radio1Frame, text="Spēlētājs 1", font=('Cascadia Mono ExtraLight', 8), variable=izveles_vertiba, value=1, command=radiobutton_izvele)
rb1.pack()

rb2 = tk.Radiobutton(radio1Frame, text="Spēlētājs 2", font=('Cascadia Mono ExtraLight', 8), variable=izveles_vertiba, value=2, command=radiobutton_izvele)
rb2.pack()

def radiobutton_izvele2():
    if izveles_vertiba2.get() == 1:
        izvades_teksts2.set(f"Izvēlēts Mini-max algoritms")
    else:
        izvades_teksts2.set(f"Izvēlēts Alfa-beta algoritms")

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

newGamebutton = tk.Button(newGameFrame, text="New Game", font=('Cascadia Mono ExtraLight', 10), command=gui_numuri)
newGamebutton.pack(padx=20, pady=20)

punktuFrame = tk.Frame(root)
punktuFrame.place(x=360, y=520)
punkti1label = tk.Label(punktuFrame, text = "1. spēlētāja punkti: 0", font = ('Cascadia Mono ExtraLight', 10))
punkti1label.pack()

punkti2label = tk.Label(punktuFrame, text = "2. spēlētāja punkti: 0", font = ('Cascadia Mono ExtraLight', 10))
punkti2label.pack()

def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About authors")
    label = tk.Label(about_window, text="Iļja Poļivko\nMārtiņš Ņikiforovs\nRaitis Bērtulis\nHaralds Popovs\nDaniela Alise Smelte\nViktors Krasnoborodjko", padx = 100, pady = 100)
    label.pack()

about_authors = tk.Button(root, text = "About authors", font = ('Cascadia Mono ExtraLight', 10), command=open_about)
about_authors.place(relx=1, x=-5, y=5, anchor="ne")

root.mainloop()
