class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self ,odr2):
        return self.price > odr2.price
        
oder1 = order("laptop", 1200)
oder2 = order("phone", 800)

print(oder1 > oder2)