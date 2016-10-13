# 计算时间差值
import time as t
# perf_counter() 返回计时器的精准时间
# process_time() 返回当前进程执行 CPU 的时间总和
        
class Time:
    def __init__(self, name="perf_counter"):
        # self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.begin = 0
        self.end = 0
        self.prompt = "未开始计时"
        self.name = name
            
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    def __add__(self, other):
        self.prompt = "一共花了"
        result = []
        '''
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if not result[index]:
                self.prompt += (str(result[index]) + self.unit[index])
        '''
        result.append(self.lasted[0] + other.lasted[0])
        self.prompt += (result[0] + '秒')
        return self.prompt
    
    def set_time(self, name):
        self.name = name
    
    def start(self):
        if self.name == "perf_counter":
            self.begin = t.perf_counter()
        elif self.name == "process_time":
            self.begin = t.process_time()
        # 没有  调用方法时 stop()
        self.prompt = "提示：请先调用stop() 停止计时"
        print("开始计时")
        
    def stop(self):
        if self.begin:
            if self.name == "perf_counter":
                self.end = t.perf_counter()
            elif self.name == "process_time":
                self.end = t.process_time()
                
            self._calc();
            print("计时结束")
        else:
            print("提示： 请开始 start() 开始计时")
            
    def _calc(self):
        self.prompt = "总共花了"
        self.lasted = []
        '''
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin(index))
            if not self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        '''
        self.lasted.append(self.end - self.begin)
        self.prompt += str(self.lasted[0]) + '秒'

        # 重新初始化
        self.begin = 0
        self.end = 0
                
    
