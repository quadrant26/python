'''
testpackage
'''
import sys
import module as tc
import M1.TempertureConversion as tc2

print("80华氏度等于 %.2f 摄氏度" % tc.f2h(80))
print("10摄氏度等于 %.2f 华氏度" % tc.c2f(10))

print(sys.path)
# 添加 模块的 搜索路径

print("10华氏度等于 %.2f 摄氏度" % tc2.f2h(10))
print("0摄氏度等于 %.2f 华氏度" % tc2.c2f(0))
