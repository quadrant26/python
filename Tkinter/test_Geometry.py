'''
布局管理器
 pack    添加顺序排列组件
 grid    按行/列 形式排列
 place    自定义组件的大小和位置
'''

from tkinter import *

root = Tk()

# listbox = Listbox(root)
# listbox.pack(fill=BOTH, expand=True)
# 
# for i in range(10):
#     listbox.insert(END, str(i))
    
Label(root, text="red", bg="red", fg="white").pack(side=LEFT)
Label(root, text="green", bg="green", fg="black").pack(side=LEFT)
Label(root, text="blue", bg="blue", fg="white").pack(side=LEFT)

root.mainloop()
