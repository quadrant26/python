import os
import os.path

# 内容替换
 
def file_raplace(file_name, oldstr, newstr):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:
        if oldstr in eachline:
            count = eachline.count(oldstr) # count
            eachline = eachline.replace(oldstr, newstr)
        content.append(eachline)

    decide = input("\n 文件 %s 中 共有 %s 个【%s】 \n您确定要把所有的【%s】替换为【%s】? \n 【YES/NO】：" % (filename, count, oldstr, oldstr, newstr))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(filename, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()

filename = input("请输入文件名：")
oldstr = input("请输入需要替换的单词或字符：")
newstr = input("请输入新的单词或字符")
file_raplace(filename, oldstr, newstr)






