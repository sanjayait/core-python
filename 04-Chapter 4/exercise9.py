def greater_num(a,b):
    if a>b:
        return f"{a} is greater"
    return f"{b} is greater"

x,y=input("enter two number comma seperated : ").split(",")
x=int(x)
y=int(y)
print(greater_num(x,y))