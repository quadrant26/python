'''
Tk Toplevel
'''

from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.title("create demo")
    
    msg = Message(top, text="I love python")
    msg.pack()

Button(root, text="创建顶级窗口", command=create).pack()

root.mainloop()
