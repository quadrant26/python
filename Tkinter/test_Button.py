'''
TKinter
'''

from tkinter import *

'''
tk 
Label            在界面上输出描述性标签
Button            按钮
'''
def callback():
    var.set("我才不信呢")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("限制性内容，请离开")
textLabel = Label(frame1, textvariable=var, justify=LEFT, padx=10)
textLabel.pack(side=LEFT)

# 图片对象
photo = PhotoImage(file="db_icon_a_list.png")  # 实例化图片对象
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="i has 18", command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()