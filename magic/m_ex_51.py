# 访问的属性不存在时
class Demo:
        def __getattr__(self, name):
                return "该属性不存在"

# 编写一个 Demo 可以获取 和 赋值
class Demo2:
        '''
        def __init__(self):
                self.x = "king"
                
        def __getattr__(self, name):
                return super().__getattr__(name)

        def __setattr__(self, name, value):
                return super().__setattr__(name, value)
        '''
        def __getattr__(self, name):
                self.name = "kibng"
                return self.name
