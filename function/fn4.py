# 局部变量和全局变量

def fun(var):
    var = 1314
    print(var, end='')

var  = 520
fun(var)
print(var)

var = 'Hi'
def fun1():
    global var
    var = 'Baby'
    return fun2(var)

def fun2(var):
    var += 'I love you'
    fun3(var)
    return var

def fun3(var):
    var = '小甲鱼'

print(fun1()) 
