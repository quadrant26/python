import random

secret = random.randint(1, 10)
# secret = 4
print("开始猜数字了\n")

temp = input("猜一下心里想的是那个数字：")
guess = int(temp)
i = 3

while (guess != secret) and (i > 0):
    
        
    if guess == secret:
        print ("我擦，竟然猜对了")
        print ("哼，可惜没有奖励")
        break;
    else:
        if guess > secret :
            print ("大了大了")
        else:
            print ("小了小了")
        i = i - 1;
        if( i > 0):
            print("再试一次：")
            temp = input("猜错了， 请重新输入吧，还剩下 %s" % i + '次机会 ：')
            guess = int(temp)
        else:
            print("你已经没有机会了！")
        
        

print("game over")
