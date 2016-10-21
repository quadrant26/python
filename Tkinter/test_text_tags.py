'''
Text
'''

from tkinter import *

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
text.tag_add("tag1", "1.7", "1.12", "1.1")
text.tag_add("tag2", "1.7", "1.12", "1.1")
text.tag_config("tag1", background="yellow", foreground="red")
text.tag_config("tag2", background="green", foreground="blue")






root.mainloop()
