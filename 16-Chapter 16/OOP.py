class Person:
    def __init__(self,first_name,last_name,age):   # Init is a constructor
        self.first_name = first_name  # Instance variable
        self.last_name = last_name
        self.age = age

p1 = Person('Sanjay','Goyal',29)
p2 = Person('priyanka','Goyal',21)

print(p1.first_name)
print(p2.last_name)