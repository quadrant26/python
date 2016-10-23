'''
标准对话框
 messagebox
 filedialog
 colorchooser

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
def callback():
    filename = filedialog.askopenfilename()
    print(filename)  # 打印文件的据对路径

Button(root, text="打开文件夹", command=callback).pack()

root.mainloop()

