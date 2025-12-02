class student:
    def __init__(self,phy,chem,math):
        self.phy = phy  
        self.chem = chem
        self.math = math
       
    
    # def calcpercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
stu1 = student(90,80,70)
print(stu1.percentage)   

stu1.phy = 100
print(stu1.percentage) 