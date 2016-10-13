class Int(int):
    def __add__(self, other):
        return int.__add__(self, other)
    
a = Int('3')
b = Int(4)
print(a-b)

'''
# 反算术运算符
__radd__            +
__rsub__            -
__rmul__            *
__rtruediv__        /
__rfloordiv__       //
__rmod__            %
__rdivmode__
__rpow__            **
__rlshift__            <<
__rrshift__            >>
__rand__                按位 与 &
__rxor__                按位 或 ^
'''

class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)
    
a = Nint(3)
b = Nint(6)
print(a+b)
print(3+b)  # 3 没有算术方法， 就会触发 b 的 radd 方法

'''
# 增量算术运算符
__iadd__            ++
__isub__            -
__imul__            *
__itruediv__        /
__ifloordiv__       //
__imod__            %
__idivmode__
__ipow__            **
__ilshift__            <<
__irshift__            >>
__iand__                按位 与 &
__ixor__                按位 或 ^
'''

'''
# 一元操作符
__neg__            定义正号的行为     +x
__pos__            定义负号的行为    -x
__abs__            当被 abs() 调用的
__invert__         按位求反的行为 -
'''

