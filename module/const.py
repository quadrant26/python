'''
提示：
	1. 需要一个 Const 类
	2. 重写 Const 的魔法方法， 指定实例对象属性修改时的行为
	3. 检查该属性时候存在
	4. 检查该属性的名字是否为大写
	5. 把 Const.NAME 当成对象来使用
'''

class Const:
	def __init__(self):
		pass
	
	def __setattr__(self, key, value):
		# 检测是否重名
		if key in self.__dict__:
			raise TypeError("常量无法改变")
		# 检测属性是否全部为大写
		if not (key.isupper()):
			raise TypeError("常量名必须由大写字母组成")
		
		self.__dict__[key] = value
			
import sys

sys.modules[__name__] = Const()
		
	
