# Fuction as a argumenst
def square(a):
    return a**2

l1=[1,2,3,4,5,6]
def my_map(f,l):
    new=[]
    for i in l:
        new.append(f(i))
    return new    
print(my_map(square,l1))   # You can use lambda exp in place of function