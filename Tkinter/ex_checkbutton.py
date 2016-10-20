from tkinter import *

'''
checkButton
'''

root = Tk()

GIRLS = ["西施", "昭君", "玉环", "貂蝉"]

v = []

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor="w")
    # anchor 设置显示对齐方式 方向的英文单词

mainloop()