# Scope
x=5 # Global variable

def func():
    global x
    x=7 # Local variable
    return x
print(x)
print(func())
print(x)    

