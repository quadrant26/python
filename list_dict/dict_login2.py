# 用户登录程序

datauser = {}

def new_user():
    prompt = "请输入用户名："
    while True:
        name = input(prompt);
        if name in datauser:
            prompt = "此用户已经被注册，请重新输入："
        else:
            break

    pwd = input("请输入密码：")
    datauser[name] = pwd
    print("注册成功， 赶紧试试登录吧 ^_^ ")

def old_user():
    prompt = "请输入用户名："
    while True:
        name = input(prompt);
        if name not in datauser:
            prompt = "您输入的用户不存在，请重新输入："
            continue;
        else:
            break

    pwd = input("请输入密码：")
    passwd = datauser.get(name);
    if pwd == passwd:
        print("欢迎进入 xxoo 系统，请点击右上角 x 结束程序")
    else:
        print("密码不正确")

def showmenu():
    prompt = '''
    |--- 新建用户： N/n ---|
    |--- 登录账户： E/e ---|
    |--- 退出程序： Q/q ---|
    |--- 请输入指令代码：
    '''
    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)
            if choice not in "NnEeQq":
                print("您输入的指令代码错误，请重新输入：")
            else:
                chosen = True

        if choice == 'q' or choice == 'Q':
            break
        elif choice == 'e' or choice == 'E':
            old_user()
        elif choice == 'n' or choice == 'N':
            new_user()
    
showmenu()
            
    
