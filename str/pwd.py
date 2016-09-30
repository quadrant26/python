'''
低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
'''
str1 = 'sdsdfssd'
print(str1.isalpha())

passwd = input("请输入密码：\n")

length = len(passwd)

print(passwd)

if length <= 8 and passwd.isalnum():
    print("这是一个低级密码")
elif 8 < length < 16 and ( passwd.isalnum()   ):
    print("这是一个中级的密码")
elif length >= 16 and passwd[0].isalpha():
    print("这是一个高级密码，已经很安全了")