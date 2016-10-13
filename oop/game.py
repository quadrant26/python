import random

class Game:
    
    gui = 1
    fish = 10
    fish_move = 1
    gui_tili = 100
    
    
    def __init__(self):
        print("Game start......")
        self.guidict = dict()
        self.guidict.setdefault("gui")
        self.guidict['gui'] = [random.randint(0,10), random.randint(0,10)]  # 设置乌龟出现的位置
        self.fishdict = {}
        
        for v in range(self.fish):
            self.fishdict.setdefault(v, [0,0])
            self.fishdict[v] = [random.randint(0,10), random.randint(0,10)]
        
    
    def guimoveing(self):
        self.gui_move = random.randint(1,2)
        
        self.gui_move -= 1
        if( self.gui_move == 0 ) or ( self.fish == 0):
            print("Game over!")


g = Game()

    