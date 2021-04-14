class Phone:    # Parent class / Base class
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=max(price,0)
        self.full_name=name+" "+model
    def full_detail(self):
        return f"{self.name} {self.model} {self.price}"

    def make_a_call(self,num):
        return f" Calling {num}"

class Smartphone(Phone):  # Derived class / Child class
    def __init__(self,name,model,price,ram,memory,camera):
        super().__init__(name,model,price)
        self.ram=ram
        self.memory=memory
        self.camera=camera

class Flagship(Smartphone):   # Multi level inheritance
    def __init__(self,name,model,price,ram,memory,camera,battery):
        super().__init__(name,model,price,ram,memory,camera)
        self.battery=battery        

p1=Phone('Nokia','X6',13000)
p2=Phone('Samsung','M30s',18000)
sp=Smartphone('Realme','X50',35000,'8 GB','64 GB','32 Mega pixel')  
fp=Flagship('Asus','Rog-3',50000,'16GB','128GB','64MP','5000Mhz')      

# Isinstance method
print(isinstance(fp,Phone))
print(isinstance(p1,Smartphone))

#issubclass method
print(issubclass(Smartphone,Phone))
print(issubclass(Smartphone,Flagship))