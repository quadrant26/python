'''
Text
'''

from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

# 插入文本
'''
text.insert(INSERT, "I love \n")
text.insert(INSERT, "python")

def show():
    print("我被点了")
'''


photo = PhotoImage(file="db_icon_a_list.png")

def show():
    text.image_create(INSERT, image=photo)

    
b1 = Button(text, text="点我点我", command=show)

text.window_create(INSERT, window=b1)


# Indexes 索引
'''
line.column  行号 1 开始，列  0 开始
line.end        某一行末尾
INSERT            对于光标的位置
END
user-defined marks
user-defined tag(tag.first, tag.last)
selection(SEL_FIRST, SEL_LAST)
window coordinate("@x,y")
embedded object name(widnow, images)
expressions
'''

root.mainloop()
