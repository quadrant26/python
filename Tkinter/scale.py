from tkinter import *

master = Tk()
'''
Scale
tickinterval=5      # 刻度表
resolution=5        # 精度  == 步长
length=200          # 长度
'''

s1 = Scale(master, from_=0, to=40, tickinterval=5, length=200)
s1.pack()

s2 = Scale(master, from_=0, to=200, orient=HORIZONTAL, resolution=15, length=600)
s2.pack()

def show():
    print(s1.get(), s2.get())

Button(master, text="获取位置", command=show).pack()

master.mainloop()