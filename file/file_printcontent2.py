import os
import os.path

# # 编写一个程序，输入 12:31 打印 12 到 31行 ，输入 21: 打印 21行到末尾 :21 开头到末尾

def view_file(filename, linenum):
    if linenum.strip() == ":":
        begin = "1"
        end = "-1"

    (begin, end) = linenum.split(":")

    if begin == "":
        begin = "1"
    if end == "":
        end = "-1"

    if begin == "1" and end == "-1":
        prompt = '的全文'
    elif begin == "1":
        prompt = "从开始到 %s " % end
    elif end == "-1":
        prompt = "从%s 到结束 " % begin
    else:
        prompt = "从第%s 行到第%s行" % (begin, end)

    print("\n 文件 %s %s 的内容如下" % (filename, prompt))

    begin = int(begin)-1
    end = int(end)
    lines = end - begin

    f = open(filename)

    for i in range(begin): # 用于消耗 begin 之前的内容
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(), end="")


    f.close()

filename = input("请输入要打开的文件 (C:\\test.txt):")
linenum = input("请输入需要显示的行数：")
view_file(filename, linenum)






