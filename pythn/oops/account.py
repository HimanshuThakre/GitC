class account:
    
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("rs.",amount,"was debited")
        print("total balance;",self.get_balance())
    #credit method  
    def credit(self,amount):
        self.balance += amount
        print("rs.",amount,"was debited")
        print("total balance;",self.get_balance())
       
        
    def get_balance(self):
        return self.balance
        
acc1 = account(5000,"1234")
acc1.debit(1000)    
acc1.credit(200)