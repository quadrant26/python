from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

line1 = w.create_line(0, 50, 200, 50, fill="yellow")
line2 = w.create_line(100, 0, 100, 100, fill="red", dash=(1, 4))
rect1 = w.create_rectangle(50, 25, 150, 75, fill="blue")

'''
移动到新位置
    coords(obj, startx, starty, endx, endy)
设置新属性
    itemconfig(obj, options)
删除对象
    delete(obj)
    
'''
w.coords(line1, 0, 25, 200, 25)
w.itemconfig(rect1, fill="red")
w.delete(line2)

Button(root, text="删除全部", command=(lambda x=ALL:w.delete(x))).pack()

root.mainloop()