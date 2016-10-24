'''
Tk Spinbox
'''

from tkinter import *

root = Tk()

w = Spinbox(root, from_=0, to=100)
w.pack()

w2 = Spinbox(root, values=("python", "video", "23234"))
w2.pack()


root.mainloop()
