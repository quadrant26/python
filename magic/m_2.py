# 工厂函数
print( type(len))
print( type(dir))
print( type(list))
print( type(int))

class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)
    def __sub__(self, other):
        return int.__add(self, other)

a = New_int(3)
b = New_int(5)
print(a+b)

'''
# 这样写会报错， 
class Try_int(int):
    def __add__(self, other):
        return self + other
    def __sub__(self, other):
        return self - other
'''
class Try_int(int):
    def __add__(self, other):
        return int(self) + int(other)
    def __sub__(self, other):
        return int(self) - int(other)
a = Try_int(3)
b = Try_int(5)
print(a + b)


'''
# 算术运算符
__add__            +
__sub__            -
__mul__            *
__truediv__        /
__floordiv__       //
__mod__            %
__divmode__
__pow__            **
__lshift__            <<
__rshift__            >>
__and__                按位 与 &
__xor__                按位 或 ^
'''