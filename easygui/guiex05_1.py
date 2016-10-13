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
maxcount = 100000
countnum = 0
scalenum = 0

filetype = {}

def get_code_lines(dir):
    os.chdir(dir)
    file_list = os.listdir(os.curdir)
    global countnum
    
    for each_file in file_list:
        if os.path.isfile(each_file):
            ext = os.path.splitext(each_file)[1]
            filetype.setdefault(ext, [0, 0])
            filetype[ext][0] += 1
            f = open(each_file, 'rb')
            for each_line in f:
                filetype[ext][1] += 1
                countnum += 1
            f.close()
        
        if os.path.isdir(each_file):
            get_code_lines(each_file)
            os.chdir(os.pardir)
            

if filename:
    get_code_lines(filename)

    if countnum < maxcount:
        scalenum = maxcount - countnum
        jindu = int(float((countnum/maxcount))*100)
        msg = "您目前共累计编写了 %d 行代码， 完成进度：%d%s \n 离10万代码还差  %d 行，请继续努力" % (countnum, jindu, '%', scalenum)
        #msg = "您目前共累计编写了" + countnum + "行代码， 完成进度：" + jindu+"\n 离10万代码还差 " + scalenum + "行，请继续努力"
        
        print(msg)
        
        for k in filetype:
            print("【%s 】源文件 %d , 源代码 %d 行" % (k, filetype[k][0], filetype[k][1]))
        
















