import os
import os.path


# 编写一个程序，单用户输入文件名和行数后，将该文件的前 N 行打印出来

def file_view(filename, linenum):
    print("\n 文件 %s 的前 %s 的内容如下：\n" % (filename, linenum))
    f = open(filename)

    for i in range(int(linenum)):
        print(f.readline(), end="")

    f.close()

filename = input("请输入要打开的文件 (C:\\test.txt):")
linenum = input("请输入需要显示该文件的前几行：")
file_view(filename, linenum)
