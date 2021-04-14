from functools import wraps
import time
l1=[1,2,3,4,5,6,7,8,9]
l2=[2,3,5,7,8,9,[5,2,3,4]]
def only_int_allow(func1):
    @wraps(func1)
    def wrap5(*args,**kwargs):
        '''This function allows only integer arguments'''
        t1=time.time()
        if all([(type(i)==int or type(i)==float) for i in args]):
            temp= func1(*args,**kwargs)
            t2=time.time()
            print(f"Time to excute programs {t2-t1} sec")    
            return temp
        else:
            return'Wrong input' 
    return wrap5           

@only_int_allow
def all_add(*args):
    total2=0
    for j in args:
        total2 +=j
    return total2
l3=list(range(10000))
print(all_add(*l3))

# l3=list(range(10000))
# print(l3)