# 用户登录程序

str1 = '''
|--- 新建用户： N/n ---|
|--- 登录账户： E/e ---|
|--- 退出程序： Q/q ---|
'''
users = {}

def login():
    name = input("请输入用户名：")
    if name not in users:
        pwd = input("请输入密码：")
        users[name] = pwd
        print("注册成功, 赶紧试试登录吧 ^_^ ")
    else:
        name = input("此用户名已经被使用，请重新输入：")
        pwd = input("请输入密码：")
        users[name] = pwd
        print("注册成功, 赶紧试试登录吧 ^_^ ")


def reg():
    name = input("请输入用户名：")
    if name not in users:
        reg();
    else:
        pwd = input("请输入密码：")
        if users[name] == pwd:
            print("欢迎进入 xxoo 系统，请点击右上角 x 结束程序")
        else:
            print("密码不正确，请重新输入")

def quits():
    print("结束程序");
        
while 1:
    print(str1)
    code = input("请输入指令代码：")
    if code == 'N' or code == 'n':
        login();
    elif code == 'E' or code == 'e':
        reg()
    elif code == 'Q' or code == 'q':
        quits()
        break; 
         
        
