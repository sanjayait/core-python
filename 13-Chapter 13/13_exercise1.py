names=['sanjay','kunno','harshal','priyanka']
def index(l,s):
    pos=-1
    for i in l:
        pos += 1
        if i==s:
             return pos
    return -1    
print(index(names,'kunno'))



# With enumerate func
def index1(a,b):
    for pos,i in enumerate(a):
        if i==b:
            return pos
    return -1
print(index1(names,'priyanka'))                        
