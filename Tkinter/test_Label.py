'''
TKinter
'''

from tkinter import *

'''
tk 
Label            在界面上输出描述性标签
Button            按钮
'''

root = Tk()

textLabel = Label(root, text="限制性内容，请离开", justify=LEFT, padx=10)
textLabel.pack(side=LEFT)

# 图片对象
photo = PhotoImage(file="db_icon_a_list.png")  # 实例化图片对象
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()