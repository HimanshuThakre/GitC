class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def show(self):
        print(f"{self.real} + {self.imag}i")
        
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return complex(newreal, newimag)
    
num1 = complex(2,3)
num1.show()
num2 = complex(5,7)
num2.show() 

num3 = num1 + num2
num3.show()