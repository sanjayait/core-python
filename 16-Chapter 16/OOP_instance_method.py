class Person:
    def __init__(self,first_name,last_name,age):   # Init is a constructor
        self.first_name = first_name  # Instance variable
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18 

p1 = Person('Sanjay','Goyal',29)
p2 = Person('priyanka','Goyal',21)

print(p1.full_name())
print(Person.full_name(p2))  # Actutal hota aesa hai
print(p2.is_above_18())