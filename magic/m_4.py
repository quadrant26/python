'''
制一个计时器类
    start    stop 启动和停止
    倒计时器对象 t1  print(t1) 直接调用 t1 会直接打印
    倒计时没有停止时  调用 stop 方法会温馨提示
    两个计时器对象可以相加
    有限的资源
    
    __str__
    __repr__
'''
import time as t

class A:
    def __str__(self):
        return ("King")
        
    def __repr__(self):
        return ("king")
    
a = A()
a
print(a)


class Timer:
    
    # 开始计时
    def __init__(self):
        self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.prompt = "未开始计时"
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
        
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop() 停止计时"
        print("计时开始")
    
    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 开始计时")
        else:
            self.end = t.localtime()
            self._clac()
            print("停止计时")
        
    def _clac(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            # 判断差值时候为 0 时不显示
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        
        # 回到初始化
        self.begin = 0
        self.end = 0
        
    
t1 = Timer()
t2 = Timer()