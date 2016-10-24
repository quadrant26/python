'''
布局管理器
 pack    添加顺序排列组件
 grid    按行/列 形式排列
 place    自定义组件的大小和位置
'''

from tkinter import *

root = Tk()

Label(root, bg="red").place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
Label(root, bg="yellow").place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
Label(root, bg="blue").place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)


root.mainloop()
