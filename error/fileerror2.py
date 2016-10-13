
try:
    f = open("a.txt")
    print(f.read())
    
except Exception as reason:
    print("这是个错误" + str(reason))
finally:
    print("我在打开文件")
