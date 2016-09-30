
def hello():
    print("hello king")

temp = hello()
print(temp)    #None

def discounts(price, rate):
    final_price = price * rate
    print("这里试图访问全局变量 old_price 值 1 ： ", old_price)
   # old_price = 50  # 在函数内部修改全局变量时， python 会在函数内部创建一个 同名的 局部变量
    return final_price

old_price = float(input("请输入原价："))
rate = float(input("请输入折扣率："))
print(type(rate), type(old_price))
new_price = discounts(old_price, rate)
print("打折后的价格是：值 2",new_price)
print("原来的价格 2 ： ",new_price)
# print("这里试图打印局部变量 final_price的值：",final_price)


def next():
    print("我在 next() 函数里面")
    prev()

def prev():
    print("我在 prev() 函数里面")

next()