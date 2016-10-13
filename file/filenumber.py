# file

import os
import os.path

# 统计当前目录下每个文件类型的大小

cwd = os.getcwd()
print(cwd)

listcwd = os.listdir(".") # 返回当前文件目录的文件
leng = len(listcwd)     # 文件的个数

for item in range(leng):
    print("%s 【%s btyes】" % (listcwd[item], os.path.getsize(listcwd[item])) )

     
def allfilr_size():
    all_file = os.listdir(os.curdir)
    file_dict = dict()

    for each_file in all_file:
        if os.path.isfile(each_file):
            file_size = os.path.getsize(each_file)
            file_dict[each_file] = file_size

    for each in file_dict.items():
        print('%s [%d Bytes]' % ( each[0], each[1]))


allfilr_size()   
    






