def capital(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return[i[::-1].title() for i in l]
    else:   
        return[i.title() for i in l]
names=['sanjay','goyal','harshal','kunno']   
print(capital(names,reverse_str=True))  
print(capital(names))  
