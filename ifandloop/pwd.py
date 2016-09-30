# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内
# 

pwds = "adwsweew"
pwd = input()
times = 3

while times > 0:
    if '*' in pwd:
        pwd = input("不能包含 * 号\n")
        continue
    else:
        if pwds != pwd:
            times -= 1
            if(times < 1):
                print("game over")
                break
            pwd = input("输入不正确，请重新输入，还剩下%s \n" % times)
        else:
            print("输入正确，欢迎进入")



