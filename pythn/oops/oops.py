# class Student:
#     college = "ABC College"
#     name = "anonymous" #class attribute
    
#     def __init__(self,name,marks):
#         self.name = name#obj atrr >= class attr
#         self.marks = marks
#         print("adding new student is database...")
    
    
# s1 = Student("prem",78)
# # print(s1.name,s1.marks)


# s2 = Student("ram",98)
# print(s2.name,s2.marks)


# class Student:
#     college = "ABC College"
    
    
#     def __init__(self,name,marks):
#         self.name = name#obj atrr >= class attr
#         self.marks = marks
#     def welcome(self):
#         print("welcome student",self.name)    
        
#     def get_marks(self):
#         return self.marks 
    
# s1 = Student("prem",78)
# s1.welcome()
# print(s1.get_marks())

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def college():
        print("ASD college of engineering")
        
    def get_avh(self):
        sum = 0
        for val in self.marks:
            sum += val  
        print("average marks:",sum/len(self.marks))

    
    
s1 = Student("prem",[99,88,77])
s1.get_avh()
s1.college()