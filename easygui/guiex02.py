# 实现一个用于登记用户账号信息的界面（如果是带 * 号的必填项，要求一定要有输入并且不能是空格）。

import easygui as g

msg = "请填写以下联系方式"
title = "帐号中心"
fieldnames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "   QQ", " *E-mail"]
fieldvalues = []
fieldvalues = g.multenterbox(msg, title, fieldnames)

while 1:
    if fieldvalues == None:
        break
    
    errormsg = ""
    for i in range(len(fieldnames)):
        option = fieldnames[i].strip()
        if fieldvalues[i].strip() == "" and option[0] == "":
            errormsg = ("【%s】 为必填项. \n\n" % fieldnames[i])
    if errormsg == "":
        break
    fieldvalues = g.multenterbox(msg, title, fieldnames, fieldvalues)
    
print("用户资料如下：%s" % str(fieldvalues))


