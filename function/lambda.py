# lambda 表达式
# 

def ds(x):
    return 2 * x + 1
print( ds(5) )


print( lambda x: 2 * x + 1 )

g = lambda x: 2 * x + 1
print( g(5))

f = lambda x,y : (x+y)*5
print(f(4,5))

# filter 

print( filter(None, [1,0,False, True]) )
print( list( filter(None, [1,0,False, True]) ) )

list1 = [1,2,3,4,5,6,7,8,9,10]
def odd(x):
    return x%2
show = filter(odd, list1)
print(list(show))

shlist = filter(lambda x: x % 2, list1)
print(list(shlist))


print(list(map(lambda x:x*2, range(1, 10))))


# lambda 表达式
# 

def fun_A(x, y=3):
    return x * y

print(fun_A(3))

f = lambda x, y=3:x*y
print( f(3))

g = lambda x : x if x % 2 else None

print( g(6) )

def fx(x):
    if x % 2:
        return x
    else:
        return None

print( fx(6) )

print( list(x for x in range(1, 100) if x % 3 == 0))
# print( list(x for x in range(1, 100) if not(x % 3) ))

h = lambda x : x % 3 == 0
h = lambda x : not(x % 3)

lsiy1 = list(filter(h, range(1,100)))
print(lsiy1)


l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

newlist = list( map(lambda x,y : [x, y], l1, l2) )
print( newlist )


def make_repeat(n):
    return lambda s : s * n

double = make_repeat(2)
print( double(8))   # 16
print( double('I love fishC')) #I love fishCI love fishC







