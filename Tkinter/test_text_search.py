'''
Text
'''

from tkinter import *
import webbrowser
import hashlib

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love python")

start = "1.0"

def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), ".")))

while True:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    else:
        print("位置是：", getIndex(text, pos))
    
    start = pos + "+1c"


root.mainloop()
