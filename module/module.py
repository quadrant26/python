'''
导入模块
1. import 模块名
2. from 模块名 import 方法名
3. import 模块名 as 新名字
'''

def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

def f2h(f):
    cel = (f - 32)/1.8
    return cel
