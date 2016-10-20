'''
TKinter
'''

from tkinter import *
from Tkinter.test_tk import theLabel

'''
tk 
Label            在界面上输出描述性标签
Button            按钮
'''

root = Tk()

photo = PhotoImage(file="db_icon_a_list.png")
theLabel = Label(root, 
                 text = "I love python",
                 justify = LEFT,
                 image = photo,
                 compound=CENTER, # 定义图片的显示方式，背景图来显示
                 font=("华康少女字体", 20), # 定义字体和字号
                 fg = "white")
theLabel.pack()
mainloop()