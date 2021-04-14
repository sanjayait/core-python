class Circle:
    count_instance=0
    pi=22/7    # Class variale
    def __init__(self,radius):
        Circle.count_instance += 1
        self.radius=radius

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instance of {cls.__name__}"

    def Circumference(self):           # Instance method
        return 2*Circle.pi*self.radius

    def Area(self):                    # Instance method
        return Circle.pi*self.radius**2

c1=Circle(5)
c2=Circle(7)
print(c1.Circumference())
print(c2.Area())
print(Circle.count_instances())