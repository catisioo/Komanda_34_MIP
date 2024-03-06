import tkinter as tk
from functions import *

# Test the function
print(generate_numbers())

#gui

root = tk.Tk()
root.geometry("1000x500")
root.title("Spēle, komanda 34")

autori = tk.Label(root, text="Iļja Poļivko,\n Mārtiņš Ņikiforovs,\n Raitis Bērtulis,\n Haralds Popovs,\nDaniela Smelte,\nViktors Krasnoborodjko")
autori.pack(padx=20, pady=20)

root.mainloop()