from functools import wraps
def print_data(any_func):
    @wraps(any_func)
    def wrap3(*args,**kwargs):
        print(f"You are calling {any_func.__name__} function")
        print(any_func.__doc__)
        return any_func(*args,*kwargs)
    return wrap3

@print_data
def addition(a,b):
    '''This function takes 2 argumensts and return there sum'''
    return a+b
print(addition(5,6))            