# 定义一个类， 实例化该类的时候，自动判断传入了多少个参数，并显示出来
class C:
    def __init__(self, *args):
        if len(args):
            leng = len(args)
            print("传入了 %d 个参数， 分别是 %s" % (leng, str(args)))
        else:
            print("并没有传入参数")

class Word(str):

    def __new__(cls, word):
        if ' ' in word:
            print("Value contains spaces. Truncating to first space")
            word = word[:word.index(" ")]
    # <
    def __lt__(self, other):
        return len(str) < len(other)
    # <=
    def __le__(self, other):
        return len(str) <= len(other)

    # >
    def __gt__(self, other):
        return len(str) > len(other)

    # >=
    def __ge__(self, other):
        return len(str) >= len(other)
        
