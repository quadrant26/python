import random

# int() 四舍五入

a = 5.5
b = 3.3
print(a+0.5)          # 四舍五入的方法
print(b+0.5)

press = random.randint(1,10);
times = 3;
guess = 0;

while (times > 0) and ( guess != press ):

    temp = input("请输入一个数字：")

    '''
    if temp.isdigit():
        guess = int(temp)
    else:
        print("您的输入不合法")
    '''
    while not temp.isdigit():
        temp = input("您的输入不合法,请重新输入：")
        
    guess = int(temp)
    times = times - 1

    if( press == guess):
        print ("你竟然猜对了！不可思议")
        print ("一点都不好玩不好玩")
    else:
        if guess > press:
            print("大了大了")
        else:
            print("小了小了")

        if(times > 0):
            print("你猜错了，请重新输入， 还剩下 %s" % (times))
        else:
            print("你的机会已经用完了")

print ("game over")



