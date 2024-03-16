import tkinter as tk
from functions import *

root = tk.Tk()

root.geometry("900x600")
root.title("1. praktiskais darbs")

currentNrLabel = tk.Label(root, text = "Current Number:", font = ('Cascadia Mono ExtraLight', 18))
currentNrLabel.pack(padx = 20, pady = 40)

div2button = tk.Button(root, text = "/2", font = ('Cascadia Mono ExtraLight', 10))
div2button.pack(padx = 20, pady = 20)

root.mainloop()

