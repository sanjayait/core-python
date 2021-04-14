l1=[1,3,5,7,9,8]
l2=[3,4,6,'sanjay']
def addition(*args):
    if all([(type(i)==int or type(i)==float) for i in args]):
        total=0
        for j in args:
            total +=j
        return total 
    else:       
        return 'wrong input'
  
print(addition(*l1))            