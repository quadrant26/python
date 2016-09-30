# file

import os
import os.path

# 输入文件名以及开始搜索的路径，搜索该文件是否存在，如遇到文件夹，进入文件夹继续搜索

def find_file(filedir, filename):

    os.chdir(filedir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in filename:
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)

        if os.path.isdir(each_file):
            find_file(each_file, filename)
            os.chdir(os.pardir)
     
filedir = input("请输入待查找的初始目录：")
peogram_dir = os.getcwd()

filename = ['.mp4', '.avi', '.rmvb']
vedio_list = []

find_file(filedir, filename)

f = open(peogram_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()



























