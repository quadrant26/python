from tkinter import *

'''
Radiobutton
'''

root = Tk()

LANGS = [("python", 1), ("perl", 2), ("ruby", 3), ("Lua", 4)]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)
    b.pack(fill='x', anchor="w")
    # fill='x' 横向填充
    # indicatoron=False  # 去掉默认的单选样式
    
# textvariable = 可变的变量
Label(root, textvariable=v).pack()

mainloop()