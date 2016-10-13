
import random
secret = random.randint(1, 10)
print(secret);

import os
import os.path

'''
# getcwd()          返回当前的路径
# chdir             改变工作目录
# listdir(path)           列举指定目录中的文件
# mkdir(path)           创建单层目录，已存在抛出异常
# makedirs(path)        创建多层目录
# remove(path)          删除文件
# rmdir(path)           删除单层目录，该目录不为空，抛出目录
# removedirs(path)      递归删除目录，从子目录逐层删除
# rename(old, new)      重命名
# system(command)       运行系统的 shell 命令
# walk(top)             遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])
# os.curdir              指代当前目录（'.'）
# os.pardir()           指代上一级目录（'..'）
# os.sep()              输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
# os.linesep()          当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）
# os.name()             指代当前使用的操作系统（包括：'posix',  'nt', 'mac', 'os2', 'ce', 'java'）
'''

'''

# import os.path 

# basename(path)            去掉目录路径，单独返回文件名
# dirname(path)             去掉文件名，单独返回目录路径
# join(path1, path2)        将path1, path2各部分组合成一个路径名
# split(path)               分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在
# splitext(path)            分离文件名与扩展名，返回(f_name, f_extension)元组
# getsize(file)             返回指定文件的尺寸，单位是字节
# getatime(file)            返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
# getctime(file)            返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
# getmtime(file)            返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

# 一下返回值为 True or False
# exists(path)              判断指定路径（目录或文件）是否存在
# isabs(path)               判断指定路径是否为绝对路径
# isdir(path)               判断指定路径是否存在且是一个目录
# isfile(path)              判断指定路径是否存在且是一个文件
# islink(path)              判断指定路径是否存在且是一个符号链接
# ismount(path)             判断指定路径是否存在且是一个挂载点
# samefile(path1, path2)    判断path1和path2两个路径是否指向同一个文件
'''
