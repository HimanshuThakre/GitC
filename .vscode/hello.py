class student :
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(" new name")
        
        
s1 = student("karan",97)
print(s1.name, s1.marks)

s2 = student("arjun",47)
print(s2.name, s2.marks)
