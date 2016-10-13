
try:
    f = open("a.txt")
    print(f.read())
    
except:
    print("文件打开错误")
finally:
    print("我在打开文件")
