import tkinter as tk

def display_word(num):
    word = {1: "one", 2: "two", 3: "three"}
    label.config(text=word[num])

root = tk.Tk()
root.title("Button Display")

button1 = tk.Button(root, text="1", command=lambda: display_word(1))
button1.pack(padx=10, pady=5)

button2 = tk.Button(root, text="2", command=lambda: display_word(2))
button2.pack(padx=10, pady=5)

button3 = tk.Button(root, text="3", command=lambda: display_word(3))
button3.pack(padx=10, pady=5)

label = tk.Label(root, text="")
label.pack(padx=10, pady=5)

root.mainloop()
