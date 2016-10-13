# file

f1 = open('G:/test.txt', 'w')
#f2 = open('G:\test.txt', 'w')
f3 = open('G://test.txt', 'w')
f4 = open('G:\\test.txt', 'w')

print(f1)
#print(f2)
print(f3)
print(f4)

f1.close();
f3.close();
f4.close();

# 1. / \ 反斜线需要转义 （/ // \\）

# 2. 默认 rt 模式 文件可读，文本模式

# 3. open('E:\\Test.bin', 'xb')     可写入以及二进制模式

# 4. 将文件对象放入列表 list(f)

# 5. 迭代打印

f = open("D:\\wamp\\www\\python\\jiayu\\test.txt")
#print(f.tell())  # 指针的位置
print(f)

for each_line in f:
    print(each_line)
f.close();

f1 = open("D:/wamp/www/python/jiayu/OpenMe.mp3")
f2 = open("D:\\wamp\\www\\python\\jiayu\\music.txt", "x")

for each_line in f1:
    print(each_line, end="")

f2.write(f1.read())

f2.close()
f1.close()
