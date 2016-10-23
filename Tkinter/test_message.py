'''
Tk Message
'''

from tkinter import *

root = Tk()

m1 = Message(root, text="这是一则消息", width=100)
m1.pack()


m2 = Message(root, text="这是一则消息kasjdfhjkasldfhasjkhdflhasjkfhashdui", width=100)
m2.pack()


root.mainloop()
