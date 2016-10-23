'''
标准对话框
 messagebox
 filedialog   
 colorchooser     颜色选择对话框

 arguments：
 title       标题
 message     消息内容
 options     参数
     default:
     icon       图标
     parent     
'''

from tkinter import *

root = Tk()

'''
askopenfilename()
asksavefilename()
指定文件的后缀
    defaultextension = ".py"
文件筛选：tuple("类型", "后缀名")
    filetypes[("PNG", ".png), ("JPG", ".jpg")]
'''

'''
colorchooser.askcolor()
'''
def callback():
    color = colorchooser.askcolor()
    print(color)  # tuple -> float ((128.5, 128.5, 255.99609375), '#8080ff')

Button(root, text="选择颜色", command=callback).pack()

root.mainloop()

