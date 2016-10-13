# 文件正常打开关闭

class FileObject:
	
	def __init__(self, filename='example.txt'):
		self.file = open(filename, 'r+')

	def __del__(self):
		self.file.close()
		del self.file



class C2F(float):
	def __new__(cls, arg=0.0):
		return float.__new__(cls, arg*1.8+32)

print(C2F(32))


class Nint(int):

	def __new__(cls, arg=0):
		if isinstance(arg, str):
			total = 0
			for each in arg:
				total += ord(each)
			arg = total

		return int.__new__(cls, arg)
