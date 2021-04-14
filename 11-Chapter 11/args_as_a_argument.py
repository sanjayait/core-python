def square_add(*args):
    total=0
    for i in args:
        total +=i**2
    return total
nums=[1,2,3,4,5]              # '*' unpack list/tuple
print(square_add(*nums))    # Here we can use * as a argument  