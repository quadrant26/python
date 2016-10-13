# 小游戏

import easygui as g

oldnum = 4
n = 0
num = g.integerbox("不妨猜一下小甲鱼心里想的是那个数字(0-10)？", "数字小游戏", lowerbound=0, upperbound=10)
while n <= 3:
    if num == oldnum:
        g.msgbox("猜对了，不玩了")
        break
    else:
        g.msgbox("猜错了");
        num = g.integerbox("不妨猜一下小甲鱼心里想的是那个数字(0-10)？", "数字小游戏", lowerbound=0, upperbound=10)
    n += 1
