# Lamda expression 
# Simple function
def add(a,b):
    return a+b

add2=lambda a,b: a+b
print(add2(4,5))     # Mostly lamda exp not used as a variable(add2,aad3)

# It is used in built in function--> Map, Redduce ,Fillter
add3=lambda a,b: a*b
print(add3(4,5))