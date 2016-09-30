# 字符串格式化
print('{0} love {1}.{2}'.format("I", "finshC", "com"))

print("{a} love {b}.{c}".format(a="I", b="finshC", c="com"))

print("\ta")

print("{{0}}".format("不打印"))

print('{0:.1f}{1}'.format(27.658, 'GB'))

# %c 格式化 字符 和 ASCII 码
print("%c" % 97)

print("%c %c %c" % (97, 98, 99))

# %s 格式化字符串
print("%s" % "i love lishan")

# %d 格式化整数
print('%d + %d = %d' % (3, 5, 8) )

# %o 格式化 八进制

print("%o" % 9)

# %x 格式化 16 进制

print("%x" % 100)

# %f 格式化定点数
print('%f' % 24.89)

# %e 科学计数法来格式化
# %E
print('%e' % 22344.34)

# %g 根据值得大小决定使用 %f 或 %e
# %G
print('%g' % 22344.34)


# 格式化操作符辅助指令
# m,n
print('%5.1f' % 27.658)
print('%.2e' % 36.232)

# - 左对齐
print('%-10d' % 5)

# + 左对齐
print('%+d' % 5)

# #
print('%#o' % 10)
print('%#X' % 108)

# 0
print('%010d' % 5)

# 0
print('%010d' % 5)

print('\a')


print("{{1}}".format("不打印", "打印"))

print("{a} love {b}.{c}".format(a="I", b="FishC", c="com"))


print('{0} {1:.2f}'.format('Pi = ', 3.1415))

'''
temp = input("您要转换的进制目标:\n")
jinzhi = input("请输入十进制数:\n")

if temp == '16':
    print('%x' % int(jinzhi))
elif temp == '8':
    print('%o' % int(jinzhi))
elif temp == '2':
    print(bin(int(jinzhi)))
'''

q = True

while q:
    temp = input("请输入数字(输入Q结束程序)：")

    if temp != 'Q':
        num = int(temp)
        print('十进制 -> 十六进制 ： %d -> 0x%x' % (num, num))
        print('十进制 -> 巴进制 ： %d -> 0o%o' % (num, num))
        print('十进制 -> 二进制 : %d -> ' % num, bin(num))
    else:
        q = False





