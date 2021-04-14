# Circle -----> Area, Circumference
class Circle:
    pi=22/7    # Class variale
    def __init__(self,radius):
        self.radius=radius
    def Circumference(self):           # Instance method
        return 2*Circle.pi*self.radius
    def Area(self):                    # Instance method
        return Circle.pi*self.radius**2

c1=Circle(5)
c2=Circle(7)
print(c1.Circumference())
print(c2.Area())