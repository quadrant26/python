# 当类的属性被访问， 修改或 设置的时候， 分别做出提醒
class MyDes:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, owner):
        pass
