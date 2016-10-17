'''
正则表达式  特殊字符
'''

import re
from re import IGNORECASE

'''
\A    字符串的开始位置
\Z     字符串的结束位置
\b    开启一个单词的边界
\B    非单词边界 （！"py " "py." "py!"）
\d     [0-9]
\D     非数字 Unicode
\s    [\t\n\t\f\v]
\S    
\w    [a-zA-Z0-9]
\W    
'''

print(re.findall(r'\bFishC\b', "FishC.com!FishC_com!(FishC)"))


p = re.compile(r"[A-Z]")
print(type(p))

print(p.search("I love FishC.com"))
print(p.findall("I love FishC.com"))

'''
编译标志

ASCII， A                    \w, \b, \s, \d 只匹配 ASCII 字符
DOTALL, S                    . 匹配任何符号， 包括换行符
IGNORECASE I                匹配时不区分大小写
LOCALE, L                    语言区域的设置
MULTLINE, M                    多行匹配 影响 ^ $
VERBOSE, X(for extended)        启用详细的正则表达式

0[0-7]+ 八进制
[0-9]
x[0-9a-fA-F] 十六进制
'''

charref = re.compile(r"""
&[#]             # 开始数字引用
(
    0[0-7]+         # 八进制
    |[0-9]+         # 十进制
    |x[0-9a-fA-F]   # 十六进制
)
;             # 结尾分号
""", re.VERBOSE)