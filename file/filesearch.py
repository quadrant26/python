# file

import os
import os.path

# 输入文件名以及开始搜索的路径，搜索该文件是否存在，如遇到文件夹，进入文件夹继续搜索

def find_file(filedir, filename):

    os.chdir(filedir)

    for each_file in os.listdir(os.curdir):
        if each_file == filename:
            print(os.getcwd() + os.sep + each_file) # 使用 os.sep 使程序更标准

        if os.path.isdir(each_file):
            find_file(each_file, filename) # 递归调用查找
            os.chdir(os.pardir)          # 递归调用完成后返回上一层目录
    

     
filedir = input("请输入待查找的初始目录：")
filename = input("请输入需要查找的目标文件：")
find_file(filedir, filename)









