import time
from functools import wraps
def show_time(func):
    @wraps(func)
    def wrap4(*args,**kwargs):
        '''This is wraper function'''
        print(f"This function execute----> {func.__name__}")
        t1 = time.time()
        temp=func(*args,**kwargs)
        t2 = time.time()
        print(f"This function took {t2-t1} sec to run")
        return temp
    return wrap4

@show_time
def square(n):
    '''this is square function'''
    return [i**2 for i in range(1,n+1)]

square(10000)    
            
