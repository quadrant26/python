from tkinter import *

master = Tk()
'''
selectmode 设置选择模式
    SINGLE  单选
    BROWSE    单选 拖动鼠标或者是方向键可以改变选项  默认值
    MULTIPLE    多选   按住 shift or ctrl
    EXTENDED 多选  按住 shift or ctrl
'''
theLB = Listbox(master, selectmode=SINGLE, height=11)
theLB.pack()
'''
theLB.insert(0, "你是猪")
theLB.insert(END, "不是猪")
'''
for item in ["皮卡丘", "比比鸟", "妙蛙种子", "杰尼龟", "喷火龙", "肯泰罗", "臭臭泥", "小磁怪", "大岩蛇", "角金鱼", "鲤鱼王"]:
    theLB.insert(END, item)

theButton = Button(master, text="del", command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack(padx=5, pady=5)

master.mainloop()