from tkinter import *

'''
Radiobutton
'''

root = Tk()

GIRLS = ["西施", "昭君", "玉环", "貂蝉"]

v = IntVar()

Radiobutton(root, text="One", variable=v, value=1).pack(anchor="w")
Radiobutton(root, text="Two", variable=v, value=2).pack(anchor="w")
Radiobutton(root, text="Three", variable=v, value=3).pack(anchor="w")
Radiobutton(root, text="Four", variable=v, value=4).pack(anchor="w")

# textvariable = 可变的变量
Label(root, textvariable=v).pack()

mainloop()