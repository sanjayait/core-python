# # How to raise error
# def add(a,b):
#     if (type(a)==int and type(b)==int):
#         return a+b
#     raise TypeError('Oops you enter invalid type')    

# print(add(5,'sanjay'))

# NotImplemented error
class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        raise NotImplementedError('You have to define this method in subclasses')

class Dog(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread=bread 

    def sound(self):
        return "Bhow Bhow"    

class Cat(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread=bread     
    def sound(self):
        return "Meow Meow"              

d1=Dog('Tinny','Pomerian')
c1=Cat('Berry','white eye')

print(d1.sound())
