class person:
    name="anonmus"
    
    # def changename(self, name):
    #     person.name = name
    
    @classmethod
    def changename(cls, name):
        cls.name = name
        
p1 = person()
p1.changename("alice")
print(p1.name)
print(person.name)