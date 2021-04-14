from functools import wraps
def decorator2(any2):
    @wraps(any2)
    def wrap2(*args,**kwargs):
        """ This is wrapper function"""
        print("this is awesome function")
        return any2(*args,**kwargs)
    return wrap2

@decorator2
def add(a,b):
    ''' This is add function'''
    return a+b        
# print(add(4,5)) 
# add(2,3)
print(add.__doc__)   