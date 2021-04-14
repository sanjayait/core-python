class Mobile:
    def __init__(self,name):
        self.name=name

class Mobilestore:
    def __init__(self):
        self.mobiles=[]

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be object of Mobile class')

m1=Mobile('Samsung')
ms1=Mobilestore()

ms1.add_mobile(m1)
print(ms1.mobiles[0].name)