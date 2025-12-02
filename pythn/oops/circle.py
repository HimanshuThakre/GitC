class circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self, pi=3.14):
        return pi * self.radius ** 2
    
    def perimeter(self, pi=3.14):
        return 2 * pi * self.radius
c1 = circle(21)
print(c1.area())
print(c1.perimeter())
        