class Customer:
    def __init__(self,name,membership,membership_expire):
        self.name = name
        self.membership = membership
        self.membership_expire = membership_expire

    @classmethod
    def from_string(cls,string):   # Class method as a constructor
        a,b,c=string.split(",")
        return cls(a,b,c)

    def full_detail(self):
        return f"{self.name} {self.membership} {self.membership_expire}"        

c1=Customer('sanjay','Gold','26/10/2025')      
c2=Customer('kunno','Silver','30/04/2024')
c3=Customer.from_string('Harshal,Bronze,06/01/2023')  # Instance created by class constructor

print(c3.full_detail())