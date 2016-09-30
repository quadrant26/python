'''
    写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
    
        要求一：递归搜索各个文件夹
        要求二：显示各个类型的源文件和源代码数量
        要求三：显示总行数与百分比
        
'''

import easygui as g
import os
import os.path

filename = g.diropenbox("浏览文件夹", default="D:\\java\\example\\jiayupython\\src")
count = 0
maxcount = 100000

def get_code_lines(dir):
    os.chdir(dir)
    file_list = os.listdir(os.curdir)
    global count
    
    for each_file in file_list:
        if os.path.isfile(each_file):
            f = open(each_file, 'rb')
            for each_line in f:
                count += 1
            f.close()
        
        if os.path.isdir(each_file):
            get_code_lines(each_file)
            os.chdir(os.pardir)
            


get_code_lines(filename)
if count > maxcount:
    print("骚年，你真厉害")
else:
    print(count)
    print("革命尚未成功，通知仍需努力")
