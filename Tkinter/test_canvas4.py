from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

rect1 = w.create_rectangle(40, 20, 160, 80, dash=(4, 4))
arc = w.create_oval(40, 20, 160, 80, fill="pink")
t = w.create_text(100, 50, text="python")

arc = w.create_oval(70, 20, 130, 80, fill="green")

root.mainloop()