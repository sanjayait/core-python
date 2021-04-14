num1=[1,3,5,7,8,2]
num2=[3,4,7,6,9,8]
def common(l1,l2):
    empty=[]
    for i in l1:
        if i in l2:
            empty.append(i)
    return empty 
print(common(num1,num2))           