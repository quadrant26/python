# 局部变量和全局变量

# 回文联第一种方法
def huiwen(var):
    new_str = var[::-1]
    length = len(var)
    result = 0
    
    
    for i in range(length):
        if( var[i] == new_str[i]):
            result += 1

    if result == length:
        print("是回文联")
    else:
        print("不是回文联")

# 回文联第二种方法
def hui(string):
    length = len(string)
    last = length -1
    length //= 2
    flag = 1

    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last = -1

        if flag == 1:
            return 1
        else:
            return 0
        
# 回文联第三种方法
def huili(var):
    list1 = list(var)
    list2 = list1.reverse(list1)

    if list1 == list2:
        print("是回文联")
    else:
        print("不是回文联 ")
    

var = input("请输入一句话：")
if hui(var) == 1:
    print("是回文联")
else:
    print("不是回文联")



def strcount(*params):
    length = len(params)
    
    for each in range(length):
        sum_e = 0
        sum_n = 0
        sum_space = 0
        sum_other = 0

        for s in params[each]:
            if s.isalpha():
                # 是字母
                sum_e += 1
            #elif s.isnumeric():
            elif s.isdigit():
                # 是数字
                sum_n += 1
            elif s.isspace():
                sum_space += 1
            else:
                sum_other += 1


        print("第",each,"个字符串共有： 英文字母 ",sum_e, "个， 数字 ",sum_n,"空格 ", sum_space," 其他字符 ",sum_other,"个")

#str1 = input("请输入第一个字符串：")
#str2 = input("请输入第二个字符串：")
str1 = "I love fishC.com."
str2 = "I love you, you love me."
strcount(str1, str2)        
