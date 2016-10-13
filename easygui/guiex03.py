'''
    提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容。
'''

import easygui as g
import os
import os.path

filename = g.fileopenbox("浏览文件夹")

print(filename)

try:
    with open(filename) as f:
        title = os.path.basename(filename)
        msg = "文件 【%s】 的内容如下：" % title
        buttonok = g.textbox(msg, title, f.read())
            
except Exception as reason:
    print("打开失败" + str(reason))

