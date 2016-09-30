def power(x,y):
    if y == 1:
        return x
    else:

        return x * power(x, y-1)


print( power(2, 4) )


def gcd(x, y):
    t = x % y
    x = y
    y = t
    return gcd(x, y)

print()

def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y)# 将前 n-1 个盘子从 x 移动到 y 上
        print(x, '-->', z) #将最底下的最后一个盘子 从 x 移动到 z 上
        hanoi(n-1, y, x, z)# 将y 上的 n-1 个盘子 移动到 z 上

hanoi(64, 'x', 'y', 'z') 
