def multyple(num1,*args):
    total=1
    for i in args:
        total *=i
    return total
print(multyple(2,3,4,5))        