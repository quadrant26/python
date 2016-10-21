'''
Text
'''

from tkinter import *
import webbrowser
import hashlib

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

contents = text.get("1.0", END)

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents = text.get("1.0", END)
    if sig != getSig(contents):
        print("Warning: 内容发生改变")
    else:
        print("风平浪静")
        
    
Button(root, text="检查", command=check).pack()






root.mainloop()
