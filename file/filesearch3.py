# file

import os
import os.path

# 输入文件名以及开始搜索的路径，搜索该文件是否存在，如遇到文件夹，进入文件夹继续搜索

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for each_key in keys:
        print("关键字出现在第 %s 行， 第 %s 个位置" % (each_key, str(key_dict[each_key])))

def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)
        begin = line.find(key, begin+1)

    return pos

def seach_in_files(filename, key):
    f = open(filename)
    count = 0
    key_dict = dict()

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)
            key_dict[count] = pos

    f.close()
    return key_dict

def search_files(key, detail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)
                
    for each_txt_file in txt_files:
        key_dict = seach_in_files(each_txt_file, key)
        if key_dict:
            print("=======================================================")
            print("在文件【%s】中找到关键字【%s】" % (each_txt_file, key))
            if detail in ["yes", "Yes", "YES"]:
                print_pos(key_dict)


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input("请问是否需要打印关键字【%s】在文件的具体位置(YES/NO)" % key)
search_files(key, detail)



























