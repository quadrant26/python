# 相减操作，去除 a 在 b 中的子字符串
class Nstr(str):
	
	def __init__(self, a):
		self.a = a

	def __sub__(self, other):
		if(self.a.find(other) != -1):
			return self.a.replace(other, "")
	'''
	
	def __sub__(self, other):
		return self.replace(other, "")
        '''
a11 = Nstr("hello, world")
a12 = Nstr("he")
print(a11 - a12)

class Nstr2(str):

	def __lshift__(self, other):
		return self[other:] + self[:other]

	def __rshift__(self, other):
		return self[:-other] + self[-other:]

a = Nstr2("You can you up, No can no BB")
print(a << 4)
print(a >> 4)

def Nstr3(str):
    '''
	def __init__(self, str=""):
		self.result = 0
		for each in str:
			self.result += ord(str)

	def __add__(self, other):
		return str.__add__(self, ord(other))

	def __sub__(self, other):
		return str.__sub__(self, ord(other))

	def __mol__(self, other):
		return str.__mol__(self, ord(other))

	def __truediv__(self, other):
		return str.__truediv__(self, ord(other))
    '''
   
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误")

    def __add__(self, other):
        return self.total + other.total
    def __sub__(self, other):
        return self.total - other.total
    def __mul__(self, other):
        return self.total * other.total
    def __truediv__(self, other):
        return self.total / other.total
    def __floordiv__(self, other):
        return self.total // other.total

class Nstr4(str):
    def __new__(cls, other):
        if isinstance(other, str):
            total = 0
            for each in other:
                 total += ord(each)
            arg = total
        return int.__new__(cls, arg)
