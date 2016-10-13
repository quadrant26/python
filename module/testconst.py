# const 模块用于让 python 支持常量操作
import const
import hello

const.NAME = "fishC"
print(const.NAME)

try:
	# 尝试修改常量
	const.NAME = "com"
except TypeError as Err:
	print(Err)

try:
	# 常量名需要大写
	const.name = "king"
except TypeError as Err:
	print(Err)

hello.hi()

'''
常量无法改变
常量名必须由大写字母组成
'''
	