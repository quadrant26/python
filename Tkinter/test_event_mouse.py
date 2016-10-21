from tkinter import *

root = Tk()

'''
事件对象
'''
def callback(event):
    print("点击位置：", event.x, event.y)

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()
'''
 Button 鼠标事件
     1     左键
     2     滚轮
     3     右键
'''

root.mainloop()