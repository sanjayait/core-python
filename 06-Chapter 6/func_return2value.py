def func(int1,int2):
    add= int1+int2
    multy= int1*int2
    return add, multy
int1,int2=(input("enter two number")).split(",")    
int1=int(int1)
int2=int(int2)
add,multy=func(int1,int2)    
print(add)
print(multy)   

# num=tuple(range(11))
# num1=list(num)
# print(num1)