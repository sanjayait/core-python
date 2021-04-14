nums=[1,2,3,4,5]
def to_power(num1,*args):
    if args:
        return[i**num1 for i in args]
    else:
        return"you did't pass args"    
   
print(to_power(3,*nums))    