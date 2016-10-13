class MyDes:
        def __get__(self, instance, owner):
                print("setting")

class Test:
        a = MyDes()
        x = a

'''
class MyDes2:
        def __init__(self, value=None):
                self.val = value

        def __get__(self, instance, owner):
                return self.val - 20

        def __set__(self, instance, owner):
                self.val = value + 10
                print(self.val)

class C:
        x = MyDes2()

if __name__ == '__main__': # 该模块被执行的话，执行下边的语句
        c = C()
        c.x = 10
        print(c.x)
'''

class MyDess:
        def __init__(self, value=None):
                self.val = value
        def __get__(self, instance, owner):
                return self.val ** 2
class Tests:
        def __init__(self):
                self.x = MyDess(3)

test = Tests()
print(test.x)
