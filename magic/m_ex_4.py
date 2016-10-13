# 计算时间差值
import time as t

class Time:
    
    def __init__(self):
        self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.lasted = []
        self.prompt = "还没开始计时"
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    
    def __add__(self, other):
        self.prompt = "一共过了"
        result = []
        for index in range(6):
            result.addend(self.lasted[index] + other.lasted[index])
            if result[index]:
                self.prompt += str(result[index]) + self.unit[index]
        return self.prompt
    
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：还没停止时间 stop()"
        print("计时开始")
        
    def stop(self):
        if not self.begin:
            self.prompt = "提示： 还没有开始计时 start()"
        else:
            self.end = t.localtime()
            self._clac()
            print("结束计时")

    
    def _clac(self):
        self.prompt = "已经过了"
        self.lasted = []
        for index in range(6):
            temp = self.end[index] - self.begin[index]
            if temp < 0:
                # 测试高位是否有得 "借" 没得 "借" 再向高位 "借"
                i = 1
                while self.lasted[index-1] < 1:
                    self.lasted[index-1] += self.borrow[index-1] - 1
                    self.lasted[index-i-1] -= 1
                    i += 1
                
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append[temp]
                
        # 由于高位随时会被借位， 所以打印要放在后面
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
                
        self.begin = 0
        self.end = 0
