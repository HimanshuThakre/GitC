# class car:
   
#     color ="blue"
#     model = "2020"  
    
# car1 = car()
# print(car1.color)  
# print(car1.model)

class car:
    def __init__(self,):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.acc = True
        
        self.clutch = True
        print("car started")
        
car1 = car()
car1.start() 