from tkinter import *

master = Tk()
'''
selectmode 设置选择模式
    SINGLE  单选
    BROWSE    单选 拖动鼠标或者是方向键可以改变选项  默认值
    MULTIPLE    多选   按住 shift or ctrl
    EXTENDED 多选  按住 shift or ctrl
    
    滚动条
    sb = Scrollbar().set
    sb.config(commamd=listbox.yview)
'''
sb = Scrollbar(master)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(master, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END, i)
    
lb.pack(side=LEFT)

sb.config(command=lb.yview)

master.mainloop()