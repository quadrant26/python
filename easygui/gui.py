'''
EasyGUI

命令行调用
    
    添加了环境变量： python easygui.py
    没有添加环境变量： 安装路径/python.exe easygui
    
IDE ( idle, pythonwin, wing)
    
    import easyhui as g
    g.egdemo()
    
导入 EasyGUI
    
    1. import easygui
                使用easygui easygui.msgbox(...)
    
    2. from easygui improt *
                使用easygui msgbox(...)
    
    3. import easygui as g
                使用easygui g.msgbox(...)

'''
import easygui as g
import sys

while 1:
    g.msgbox("hi，欢迎进入第一个界面小游戏 ^_^")
    
    msg = "您希望掌握多少个技能呢？"
    title = "标题"
    choices = ["java", "python", "php", "javascript"]
    
    # not that we convert choice to string, in case
    # the user canceled the choice, and we not None 
    choice = g.choicebox(msg, title, choices) 
    
    g.msgbox("你的选择是：" + str(choice), "结果")
    
    msg = "你希望重新开始选择么？"
    
    if g.ccbox(msg, title): # show a Continue/Cancel dialog
        pass                # user chose continue
    else:
        sys.exit(0);        # easygui chose cancel
    

