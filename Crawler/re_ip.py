'''
正则表达式
'''

import re

print(re.search("FishC", "I love FishC.com"))

print(re.search(r'Fish', "I love FishC.com"))

print(re.search(r'\.', "I love FishC.com"))

print(re.search(r'\d', "I love 123 FishC.com"))

print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', "192.169.111.111"))

print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', "192.169.1.1"))

print(re.search(r'[aeiou]', "I love FishC.com"))

print(re.search(r'[aeiouAEIOU]', "I love FishC.com"))

print(re.search(r'[a-z]', "I love FishC.com"))

print(re.search(r'[2-9]', "I love 123 FishC.com"))

print(re.search(r'ab{3}c', "abbbc"))
print(re.search(r'ab{3, 10}c', "abbbbbbbbbbbc"))

print(re.search(r'[0-255]', "188"))
print(re.search(r'[0-2[0-5][0-5]', "188"))
print(re.search(r'[01]\d\d|2[0-4]\d|25][0-5]', "188"))

print(re.search(r'(([01]\d\d|2[0-4]\d|24[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])', '168.1.1.1'))

print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|24[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '168.1.1.1'))
