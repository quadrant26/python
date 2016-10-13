# 属性访问的魔术方法
class C:
    def __getattr__(self, name):
        print(1)

    def __getattribute__(self, name):
        print(2)

    def __setattr__(self, name, value):
        print(3)

    def __delattr__(self, name):
        print(4)
        

class C1:
    def __getattr__(self, name):
        print(1)
        return super().__getattr__(name)

    def __getattribute__(self, name):
        print(2)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print(3)
        return super().setattr__(name, value)

    def __delattr__(self, name):
        print(4)
        super().__delattr__(name)

class Counter:
    def __init__(self):
        self.counter = 0 # 赋值时会调用 __setattr__ 方法

    def __setattr__(self, name, value):
        # self.counter += 1 # 只有在调用后才能设置 self.counter 的值 这里的 counter 还没有定义，所以没法 += 1
        super().__setattr__(name, value)

    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)
