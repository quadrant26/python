# file

import os
import os.path

# 统计当前目录下每个文件类型的文件数

allfiles = os.listdir(".") # 返回当前文件目录的文件
dict_type = dict();

for each_file in allfiles:
    if os.path.isdir(each_file):
        dict_type.setdefault('文件夹', 0)
        dict_type['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        dict_type.setdefault(ext, 0)
        dict_type[ext] += 1

for each_type in dict_type.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, dict_type[each_type]))

     





























