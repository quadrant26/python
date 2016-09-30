# 求兔子的总数
# 

def tuzi(n):
    result = 0
    if n == 1:
        result = 1
    elif n == 2:
        result = 1
    elif n > 2:
        result = tuzi(n-1) + tuzi(n-2)

    return result

print(tuzi(20))

def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print("输入有误")
        return -1

    while (n-2)>0:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        n -= 1

    return n3

result = fab(20)
print(result);