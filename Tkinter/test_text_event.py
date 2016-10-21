'''
Text
'''

from tkinter import *
import webbrowser

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

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

# tag_raise()    # 提高优先级
# tag_lower()    # 降低优先级
text.insert(INSERT, "I love python")

text.tag_add("link", "1.7", "1.13")
text.tag_config("link", foreground="blue", underline=True)

def show_hand_cursor(event):
    text.config(cursor="arrow")
    
def show_xterm_cursor(event):
    text.config(cursor="xterm")
    
def click(event):
    webbrowser.open("http://www.baidu.com/")

text.tag_bind("link", "<Enter>", show_hand_cursor)
text.tag_bind("link", "<Leave>", show_xterm_cursor)
text.tag_bind("link", "<Button-1>", click)






root.mainloop()
