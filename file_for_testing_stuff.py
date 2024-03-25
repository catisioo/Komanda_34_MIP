import tkinter as tk
from functions import *

root = tk.Tk()

root.geometry("900x600")
root.title("1. praktiskais darbs")

currentNrLabel = tk.Label(root, text = "Current Number:", font = ('Cascadia Mono ExtraLight', 18))
currentNrLabel.pack(padx = 20, pady = 40)

def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About authors")
    label = tk.Label(about_window, text="Iļja Poļivko\nMārtiņš Ņikiforovs\nRaitis Bērtulis\nHaralds Popovs\nDaniela Alise Smelte\nViktors Krasnoborodjko", padx = 100, pady = 100)
    label.pack()

about_authors = tk.Button(root, text = "About authors", font = ('Cascadia Mono ExtraLight', 10), command=open_about)
about_authors.place(relx=1, x=-5, y=5, anchor="ne")

root.mainloop()

