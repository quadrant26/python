import easygui as g
import sys
from test.test_importlib.import_.test___package__ import Setting__package__

# g.msgbox(msg, title, ok_button, image, root)
# 参数列表 
g.msgbox("Hello, world!")

if g.ccbox():
    pass
else:
    pass

# continue cancel
choices = ["愿意", "不愿意", "等有钱的时候再说"]

# 选择
g.choicebox("您愿意花钱么", "cesde", choices=choices)

# 按钮组件
# g.buttonbox(msg, title, choices, image, root)
g.buttonbox("您愿意花钱么", "cesde", choices=choices, image=None, root=None)
# 在 buttonbox 里面选择图片
# g.buttonbox("您愿意花钱么", "cesde", choices=choices, image='url', root=None)  # 图像仅支持 gif 格式

# g.ynbox(msg, title, choices, image)
g.ynbox("shall we continue?", title="", choices=("yes", "no"), image=None)

# indexbox
g.indexbox("shall we continue?", title="", choices=("yes", "no"), image=None)

# boolbox
g.boolbox("shall we continue?", title="", choices=("yes", "no"), image=None)

# 为用户提供一系列的选项
g.choicebox("shall we continue?", title="", choices=("yes", "no"))


# 提供一个列表，可以选择多个
g.multchoicebox("shall we continue?", title="", choices=("yes", "no")
                
'''

# 让用户输入信息
g.enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)
# enterbox() 为用户提供一个最简单的输入框，返回值为用户输入的字符串。默认返回的值会自动去除首尾的空格，如果需要保留首尾空格的话请设置参数 strip=False。

integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments)
# integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值，否则会要求用户重新输入。  
               
multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())


multenterbox() 为用户提供多个简单的输入框，要注意以下几点：
    如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
    如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
    如果用户取消操作，则返回域中的列表的值或者None值。
'''
'''
# 让用户输入密码
# passwordbox() 
passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)

multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())
# multpasswordbox() 跟 multenterbox() 使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式（"*"）：              
                

# 显示文本
textbox(msg='', title=' ', text='', codebox=0)
#testbox() 函数默认会以比例字体（参数 codebox=1 设置为等宽字体）来显示文本内容（会自动换行哦），这个函数适合用于显示一般的书面文字。              
codebox(msg='', title=' ', text='')
# codebox() 以等宽字体显示文本内容，相当于 textbox(codebox=1)


# 目录和文件
diropenbox(msg=None, title=None, default=None)
# diropenbox() 函数用于提供一个对话框，返回用户选择的目录名（带完整路径哦），如果用户选择"Cancel"则返回 None。              
fileopenbox(msg=None, title=None, default='*', filetypes=None)

'''

'''
fileopenbox() 函数用于提供一个对话框，返回用户选择的文件名（带完整路径哦），如果用户选择"Cancel"则返回 None。
关于 default 参数的设置方法：
    default 参数指定一个默认路径，通常包含一个或多个通配符。
        如果设置了 default 参数，fileopenbox() 显示默认的文件路径和格式。
    default 默认的参数是'*'，即匹配所有格式的文件。
    
    example:
        default="c:/fishc/*.py" 即显示 C:\fishc 文件夹下所有的 Python 文件。
        default="c:/fishc/test*.py" 即显示 C:\fishc 文件夹下所有的名字以 test 开头的 Python 文件。
'''
filesavebox(msg=None, title=None, default='', filetypes=None)
# filesavebox() 函数提供一个对话框，让用于选择文件需要保存的路径（带完整路径哦），如果用户选择"Cancel"则返回 None。


# 记住用户的设置
# EgStore

user = "11"
server = "xx"
setting.userid = user
setting.targetServer = server
setting.store()



# 捕获异常
exceptionbox()

try:
    print("I love Fi")
    int("sdfsfd")
except:
    exceptionBox()




def msgbox(msg="(Your message goes here)", title="", ok_button="ok"):
    pass

msgbox("我会学会编程的", ok_button="加油")
