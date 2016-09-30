'''
    提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容。
    检测文件变化，如果有变化，则另存为
'''

import easygui as g
import os
import os.path

filename = g.fileopenbox("浏览文件夹")

try:
    with open(filename) as f:
        title = os.path.basename(filename)
        msg = "文件 【%s】 的内容如下：" % title
        f_read = f.read()
        text_after = g.textbox(msg, title, f_read)
        
        if f_read == text_after[:-1]:
            # textbox 的返回值会追加一个换行符
            print("想让")
        else:
            choices = ["覆盖保存", "放弃保存", "另存为"]
            status = g.indexbox("检测到文件内容发生改变，请选择以下操作", "警告", choices)
            
            if status == 0: # 覆盖保存
                f.write(text_after)
                with open(filename, 'w') as old_file:
                    old_file.write(text_after[:-11]);
            elif status == 1: # 放弃保存
                pass
            elif status == 2: # 另存为
                statuson = g.filesavebox("msg", "另存为", filetypes=["*.txt"])
                '''
                if statuson != None:
                    f1 = open("a.txt", "x")
                    f1.write(text_after)
                    f1.close()
                '''
                if os.path.splitext(statuson)[1] != 'txt':
                    statuson += ".txt"
                with open(statuson, 'w') as new_file:
                    new_file.write(text_after[:-1])
                    
        
        
            
except Exception as reason:
    print("打开失败" + str(reason))

