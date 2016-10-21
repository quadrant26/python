'''
Text
'''

from tkinter import *
import webbrowser
import hashlib

root = Tk()

text = Text(root, width=30, height=5, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT, "I love python")


# 每次只撤销一次 ，将 autospearators=False 
# 绑定 <key> 

def callback(event):
    text.edit_separator()
    
text.bind("<Key>", callback)


def show():
    text.edit_undo()
    
Button(root, text="撤销", command=show).pack()


root.mainloop()
