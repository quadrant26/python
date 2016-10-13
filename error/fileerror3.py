
try:
    int("abc")
    a = [1,2,3]
    print(a[3])
    f = open("a.txt")
    print(f.read())
    
except (ValueError, IndexError) as reason:
    print(str(reason))
finally:
    print("我在打开文件")
