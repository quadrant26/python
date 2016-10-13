# 小游戏

import random
import easygui as g

g.msgbox("hi，欢迎进入第一个界面小游戏")
secret = random.randint(1,10)

msg = "猜一下我现在想的是哪个数字（1~10）"
title = "数字小游戏"
guess = g.integerbox(msg, title, lowerbound=0, upperbound=10)

while True:
    if guess == secret:
        g.msgbox("你是蛔虫么")
        g.msgbox("猜对了也没有奖励")
        break
    else:
        if guess > secret:
            g.msgbox("大了大了")
        else:
            g.msgbox("小了小了")
        guess = g.integerbox(msg, title, lowerbound=0, upperbound=10)
        
g.msgbox("GAME OVER")
