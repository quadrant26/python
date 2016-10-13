class Ticket:
    
    pice = 100
    weekday = 1.2
    child = 0.5
    
    def normal(self, num, numchild):
        all_scoure = num*self.pice + numchild*self.child*self.pice
        print(all_scoure)
    
    def weekmondy(self, num, numchild):
        all_scoure = num*self.pice + numchild*self.child*self.pice
        print(all_scoure*self.weekday)
        
t1 = Ticket()
t1.normal(2, 1);

class Tictets:
    
    def __init__(self, weekday=False, child=False):
        self.exp = 100
        if weekday:
            self.inc = 1.2
        else:
            self.inc = 1
        
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    
    def clacPrice(self, num):
        return self.exp * self.inc * self.discount * num
    
ad = Tictets()
child = Tictets(child=True)
print("2个成人 + 1个小孩的平日票价为 ： %.2f" % (ad.clacPrice(2) + child.clacPrice(1)))
    