def outer_func():
    def inner_func():
        print("You are in inner function")
    return inner_func

outer_func()()        

# Example
def to_power(x):
    def cal_power(n):
        return x**n
    return cal_power

print(to_power(4)(3))        