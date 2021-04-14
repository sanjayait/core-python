# Decorators--> enhance functiionality of other function
def decorator1(any_func):
    def wrap_func():
        print("this is awasome",end=(" "))
        any_func()
    return wrap_func    

@decorator1
def func1():
    print('funtion 1')

def func2():
    print('function 2')    

# decorator1(func1)()
func1()  