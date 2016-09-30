# 函数

def myFirstFunction():
    print("这是我创建第一个函数")
    print("感谢CCTV， 感谢MTV， 感谢CTV")

myFirstFunction()
# 调用 未定义的函数 直接会报错
# mySecondFunction()

def add(num1, num2):
    result = num1 + num2
    print(result)

add(3,5)

def add2(num1, num2):
    return num1+num2;

print(add2(4, 6))


# 函数 扩展

def power(x, y):
    result = x
    for n in range(1, y):
        result = result * x
    return result

s = power(3, 3)
# print(s)

def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t
    print(x)

gcd(10, 25)

def dec2bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
        #print(temp)

    while temp:
        result += str(temp.pop())

    return result
    
print(dec2bin(7))  
            






# __doc__

def myfirstFunction(name):
    '函数定义过程中name叫形参'
    print("感谢cctv")
    #这是一个注释
    print(name+ "haha")

myfirstFunction('test');
print( myfirstFunction.__doc__ )


def saysome(name, words):
    print (name + words)

saysome(name="king =>", words="编程改变世界")


def saysome2(name="wang", words="编程改变世界"):
    print (name + "->" + words)

saysome2()
saysome2("hunzhang")

def normal(*params):
    print('参数的位置长度为：' , len(params))
    print("第二个参数为：" ,params[1])

normal(1, 'test', 3, 7, 8, 8)

def normal2(*params, exp = 2):
    print('参数的位置长度为：' , len(params))
    print("第二个参数为：" ,params[1])

































