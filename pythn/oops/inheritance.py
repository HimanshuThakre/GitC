class Car:
    @staticmethod
    def start():
        print("car started")    
    
    @staticmethod
    def stop():
        print("car stopped")
        
class toyotcar(Car):
    def __init__(self, brand):
        self.branf = brand
        
class fortuner(toyotcar):
    def __init__(self,type):
        self.type = type
        
car1 = fortuner("suv")
Car.start()

        