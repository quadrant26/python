
class Stack:
    def __init__(self):
        self.s = "fishc"
    
    def isEmpty(self):
        if self.s:
            return True
        else:
            return False
    
    def push(self, x):
        self.s = str(x) + self.s
        print(self.s)
    
    def pops(self):
        one = self.s[0]
        self.s = self.s[1:]
        print( one )
    
    def bottom(self):
        print( self.s[len(self.s)-1] )
    
    def top(self):
        print( self.s[0] )
    
s = Stack()
s.push(3)
s.pops()
s.top()
s.bottom()


class Stacks:
    
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)
            
    def isEmpty(self):
        return not self.stack
    
    def push(self, obj):
        self.stack.push(obj)
    
    def pop(self):
        if not self.stack:
            print("警告，栈为空")
        else:
            return self.stack.pop()
        
    def top(self):
        if not self.stack:
            print("警告，栈为空")
        else:
            return self.stack[-1]
    def bottom(self):
        if not self.stack:
                print("警告，栈为空")
        else:
            return self.stack[0]
        
        
        