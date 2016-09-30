# 写一个程序，判断给定年份是否为闰年

temp = input("请输入一个年份：")
while not temp.isdigit():
    temp = input("请重新输入：")

year = int(temp)
print (year)

if ((year/400) == int(year/400)):
    print (temp + "年是闰年")
else:
    if (year/4 == int(year/4)) and (year/100 == int(year/100)):
        print(temp + "年是闰年")
    else:
        print(temp + "年不是是闰年")
