# 递归

def recursion():
    return recursion()

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

def digui(n):
    if n == 1:
        return 1
    else:
        return n * digui(n-1)

print(digui(5))

print( factorial(5) )


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

print(gcd(10, 40))

















