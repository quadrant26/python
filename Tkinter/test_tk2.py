'''
TKinter
'''

import tkinter as tk

class App:
    
    def __init__(self, master):
        frame = tk.Frame(master)
        # side = tk.LEFT   设置位置
        # padx            边距
        # pady            边距
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        '''
        tk.Button(frame, text=按钮内容, fg=前景色, bg="背景色", command=按钮被点击时做的动作)
        '''      
        self.hi_there = tk.Button(frame, text="打招呼", fg="blue", command=self.say_hi)
        self.hi_there.pack()
        
    def say_hi(self):
        print("hello, word")
        

root = tk.Tk()
app = App(root)

root.mainloop()
