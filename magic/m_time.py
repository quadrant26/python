'''
定制一个计时器类
    start    stop 启动和停止
    倒计时器对象 t1  print(t1) 直接调用 t1 会直接打印
    倒计时没有停止时  调用 stop 方法会温馨提示
    两个计时器对象可以相加
    有限的资源
    
    __str__
    __repr__
'''
import time as t

class MyTimer:
    
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.prompt = "未开始倒计时..."
        self.lasted = []
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
    
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用 stop() 停止计时"
        print("计时开始......")
    
    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 进行计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束....")
        
    # 内部方法计算运算时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下轮时初始化变量
        self.begin = 0
        self.end = 0

t1 = MyTimer()
t1
print(t1)
t1.start()
t.sleep(3)
t1.stop()

t2 = MyTimer()
t2
t2.start()
t.sleep(9)
t2.stop()

print(t1+t2)

            
            
            
