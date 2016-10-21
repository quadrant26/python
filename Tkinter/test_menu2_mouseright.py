from tkinter import *

root = Tk()

def callback():
    print("你好...")

menubar = Menu(root, tearoff=False)

menubar.add_command(label="撤销", command=callback)
menubar.add_command(label="重做", command=callback)

frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)
    
frame.bind("<Button-3>", popup)


root.mainloop()