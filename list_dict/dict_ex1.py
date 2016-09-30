# dict

str1 = '''
|--- 欢迎进入通讯录程序 ---|
|--- 1: 查询联系人资料 ---|
|--- 2: 插入新的联系人---|
|--- 3: 删除已有联系人---|
|--- 4: 退出通讯录程序---|
'''
print(str1);
dict1 = {};

while True:
    code = int(input("请输入相关的指令代码： "))
    if code == 1:
        people = input("请输入联系人姓名:");
        if people in dict1:
            print(people+":"+dict1[people])
        else:
            print(people + "不存在")
        
    elif code == 2:
        people = input("请输入联系人姓名:");
        if people in dict1:
            print("您输入的姓名在通讯录中已存在 --->>" + people + " : " + dict1[people])
            tips = input("是否修改用户资料（YES/NO）:")
            if tips == 'YES':
                number =  input("请输入用户联系电话：")
                dict1[people] = number
            elif tips == 'NO':
                continue;
        else:
            number = input("请输入用户联系电话：")
            dict1[people] = number
    elif code == 3:
        people =  input("请输入联系人姓名:");
        if people in dict1:
            del(dict1[people])
            # dict1.pop(people)     # 可以使用 pop 方法
            print("删除成功")
        else:
            print("没有该用户")
    elif code == 4:
        print("|---  感谢您使用通讯录程序 ---|")
        break;
    
