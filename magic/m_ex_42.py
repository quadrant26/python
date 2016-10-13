# 计算时间差值
import time as t
        
class Time:
    def __init__(self, func, number=100000):
        # self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.begin = 0
        self.end = 0
        self.prompt = "未开始计时"
        self.default_time = t.perf_counter
        self.func = func
        self.number = number
            
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共花了 %.2f 秒" % result
        return prompt
    
    # 设置定时器为 t.perf_counter or t.process_time
    def set_time(self, name):
        if name == "perf_counter":
            self.default_time = t.perf_counter
        elif name == "process_time":
            self.default_time = t.process_time
        else:
            print("您的输入有误！")
            
    def timing(self):
        self.begin = self.default_time()
        for i in range(self.number):
            self.func()
        self.end = self.default_time()
        self.lasted = self.end - self.begin
        self.prompt = "总共花了 %.2f 秒" % self.lasted
                
    
