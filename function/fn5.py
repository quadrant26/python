# 内置函数 和 闭包

count = 5
def myfun():
    count = 10
    print(count)

myfun()
print(count)

# global 将变量提升为 全局变量
def myfun1():
    global count
    count = 15

myfun1()
print(count)

def fun1():
    print("fun1() 正在被调用")
    def fun2():
        print("fun2() 正在被调用")

    fun2()

fun1()

def funx(x):
    def funy(y):
        return x * y
    return funy

i = funx(8)
print(i)
print(i(4))

def fn1():
    x = 5
    def fn2():
        x *= x
        return x
    return fn2()

# fn1()  # 这样调用会报错

# 将变量 用 数组的形式 进行组合
def fnn1():
    x = [5]
    def fnn2():
        x[0] *= x[0]
        return x[0]
    return fnn2()

print(fnn1())


# nonlocal 将变量变成 局部变量
def fna1():
    x = 5
    def fna2():
        nonlocal x
        x *= x
        return x
    return fna2()

print(fna1())  # 这样调用会报错



# 内置函数 和 闭包

def funout():
    def funIn():
        print('宾果，你成功访问到我了')
    return funIn()

i = funout()

def funout2():
    def funIn2():
        print('宾果，你成功访问到我了')
    return funIn2

i1 = funout2()
i1()

def funx3():
    x = 5
    def funy():
        nonlocal x
        x += 1
        return x
    return funy

a = funx3()
print(a())
print(a())
print(a())
