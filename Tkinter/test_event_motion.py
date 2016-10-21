from tkinter import *

root = Tk()

'''
事件对象
'''
def callback(event):
    # print(event.char)
    print("当前位置：", event.x, event.y)

frame = Frame(root, width=200, height=200)
# frame.bind("<Key>", callback)
frame.bind("<Motion>", callback)    # 当鼠标移动在窗口的时候就进行响应
frame.focus_set()  # 设置焦点
frame.pack()
'''
    Key
        KeyPress         键盘按下
        KeyRelease       键盘抬起
        <KeyPress-A>     按下键盘上的A键
        <Control-Shift-KeyPress-A>    同时按下了Control、Shift、A三键。
    
    Motion    当鼠标移入的时候就进行响应
    
    Configure     窗口尺寸发生改变
    Enter         鼠标进入组件的时候触发事件
    Leave         鼠标离开组件
    
    windows
        MouseWheel
        
'''

root.mainloop()