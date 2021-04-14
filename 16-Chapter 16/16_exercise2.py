class Laptop:
    def __init__(self,brand,model,price):
    # Instance variable
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand+" "+model
    def discount(self,n):
        return self.price*(100-n)/100    

laptop1=Laptop('HP','au114tx',63000)
laptop2=Laptop('Dell','Inspire',45000)
# print(laptop2.laptop_name)
print(laptop1.discount(20))