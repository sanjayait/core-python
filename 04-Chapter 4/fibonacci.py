def fibonacci(a):
    x=0
    y=1
    if a==1:
        print(x)
    else:
        print(x,y ,end=" ")        
        for i in range(a-2):
            z=x+y
            x=y
            y=z
            print(z,end=" ")
# num=(input("enter any number : "))
print(fibonacci(25))    