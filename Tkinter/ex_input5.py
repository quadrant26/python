from tkinter import *

'''
Entry         输入框
'''

root = Tk()

def test1(content, reason, name):
    if content == "king":
        print("正确")
        print(content, reason, name)
        return True
    else:
        print("错误")
        print(content, reason, name)
        return False
    
def test2():
    print("我被调用了")
    return True

Label(root, text="帐号：").grid(row=0, column=0)
Label(root, text="密码：").grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()

# invalidcommand 错误调用此方法
testCMD = root.register(test1)
e1 = Entry(root, textvariable=v1, validate="focusout", validatecommand=(testCMD, "%P", "%v", "%W"), invalidcommand=test2) 
e2 = Entry(root, textvariable=v2, show="*")
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("帐号： %s" % e1.get())
    print("密码： %s" % e2.get())
    
Button(root, text="芝麻开门", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1,sticky=E, padx=10, pady=5)
# idle 打开的点击退出无法退出

mainloop()