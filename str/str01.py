#  字符串
str1 = "I love fishc.com"
print(str1[:6])

print(str1[5])

str2= str1[:6] + "插入的字符串" + str1[:6]
print(str2)

# capitailze() 将字符串第一个字符改成大写
print("xie".capitalize())

# casefold() 全部转为小写
print()

# center(width)      用空格填充

# count(sub, [start, end])  查看子字符串在字符串出现的次数

# encode

#endswith(sub, [start, end])  查看字符串时候是 子串 结束

# expandtabs([tabsize=8]) 将 \t 转为空格， 默认 空格长度为 8

# find(sub, [start, end])       找到子串出现的位置，找不到返回 -1

# index(sub, [start, end])      找不到抛出异常

# isalnum()     至少有一个字符并且都是字母或数字返回 True

# isalpha()     至少有一个字符并且所有字符都是字母返回

# isdecimal()   只包含十进制数字

# isdigit   只包含数字

# islower   至少包换一个区分大小的字符，且都是小写

# isnumeric()   只包含数字字符

# isspace()     只包含空格

# istitle()         所有单词大写开始，其他字母是小写

# isupper()         至少包换一个区分大小的字符，且都是大写

# join(sub)             以字符串进行连接

# ijust(width)           返回一个左对齐的字符串， 填充至长度

# lower()               转成小写

# istrip()                  去掉左边的所有空格

#partition(sub)      找到字符串 sub 将字符串分成一个 3元组 （pre_sub, sub, fol_sub）

#replace(old, new, [count])

#rfind(sub, [start, end])

# rindex(sub, [start, end])

# rjust(width)

# tpartition(sub)

# rstrip()

#split(sep=None, maxsplit=-1)

# splitlines(([keepends]))

#startswith(prefix, [start, end])

# strip([chars])

# swapcase()

# title()

# translate(table)

# upper()

# zfill(width)
# 


# 定义一个多行字符串
str11= '''alkjfasf
asldfjlsjdf'''

str12 = 'skhfksdf\ 
skjfhksfj\
sdfjhsjfs'

str13 = ('kjshfjkhskjadf'
         'askjhfkjshfdkj'
         'askjhfdkjsa')

# 不赋值的情况下  ''' 代表多行注释

# file1 = open(r'C:\windows\temp\readme.text', 'r')

str2 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'

s = str2[16:29]
s2 = str2[-45:-32]
print(str2.index("\"", 0 ,len(str2)))
print(str2.find("\""))
print(str2.count("\""))
print(s)
print(s2)

print(str2[20:-36])

str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str1[::3])






















