'''
正则表达式的方法
'''

'''
search(pattern, str, flags)
search(pattern[, ])
'''

import re

result = (re.search(r" (\w+) (\w+)", "I love FishC.com"))

print(result.group())
print(result.group(1))

print(result.start())
print(result.end())
print(result.span())