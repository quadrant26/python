'''
布局管理器
 pack    添加顺序排列组件
 grid    按行/列 形式排列
 place    自定义组件的大小和位置
'''

from tkinter import *

root = Tk()

photo = PhotoImage(file="start-bg.png")
Label(root, image=photo).pack()

def callback():
    print("center")
    
Button(root, text="click", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
