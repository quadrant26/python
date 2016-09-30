
tuple1 = (1,2,3,5,3,2,1)
print(tuple1[1])
print(tuple1)

tuple2 = tuple1[:]
print(tuple2)

# 如果元组只有一个元素，在元素后面加上一个逗号 tuple1 = (1,) tuple2 = 1,

tuple3 = ("红星", "承影", "轩辕", "迷途")
tuple4 = tuple3[:2] + ("意境",) + tuple3[2:]
print(tuple4)


x,y,z = 1,2,3
print(type(x))
h = x,y,z
print(type(h))

tuple1 = (x**2 for x in range(10))
print(tuple1)

print(tuple1.__next__())
print(tuple1.__next__())
print(tuple1.__next__())
