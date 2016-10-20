from tkinter import *

'''
Radiobutton
'''

root = Tk()

group = LabelFrame(root, text="最好的脚本语言？", padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [("python", 1), ("perl", 2), ("ruby", 3), ("Lua", 4)]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor="w")
    # fill='x' 横向填充
    # indicatoron=False  # 去掉默认的单选样式
    
# textvariable = 可变的变量
Label(root, textvariable=v).pack()

mainloop()