'''
正则表达式 元字符
'''

import re

print(re.search(r'FishC', "I love FishC.com"))

print(re.search(r'Fish(C|D)', "I love FishC.com"))
print(re.search(r'Fish(C|D)', "I love FishE.com"))

print(re.search(r'^FishC', "I love FishC.com"))

print(re.search(r'[^Fish]', "I love FishC.com"))

print(re.search(r'FishC&', "I love FishC.com"))

print(re.search(r'FishC$', "I love FishC"))
print(re.search(r'(FishC)\1', "FishCFishC"))

print(re.search(r'(FishC)\060', "FishCFishC0"))

print(re.search(r'(FishC)\141', "FishCFishCa"))

print(re.search(r'.', "FishCFishCa"))
print(re.search(r'\.', "FishCFishCa"))
print(re.search(r'[.]', "FishCFishCa"))

print(re.findall(r'[a-z]', "FishC.com"))
print(re.findall(r'[\n]', "FishC.com\n"))
print(re.findall(r'[^a-z]', "FishC.com\n"))
print(re.findall(r'[a-z^]', "FishC.com\n^"))

print(re.findall(r'FishC{3}', "FishCCCC"))

# * + ?
# {m ,n}
print(re.search(r'(FishC){1,3}', "FishCFishC"))
print(re.search(r'(FishC){1, 5}', "FishCFishC"))

s = "<html><title>I love FishC.com</title></html>"
print(re.search(r"<.+>", s))
print(re.search(r"<.+?>", s))









