class employees:
    def __init__(self, role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary  
    def showdetails(self):  
        print("role=", self.role, " dept=", self.dept, " salary=", self.salary)
       
class engineer(employees):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("engineer", "development", 70000)
enng1 = engineer("Alice", 30)
enng1.showdetails() 