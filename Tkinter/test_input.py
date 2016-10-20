from tkinter import *

'''
Entry         输入框
'''

root = Tk()

e = Entry(root)
e.pack(padx=20, pady=20)

e.delete(0, END)
e.insert(0, "默认文本...")

mainloop()