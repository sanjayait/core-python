# example define a function
# cube_finder(3)
# output---> {1:1,2:8,3:27}

def cube_finder(n):
    empty={}
    for i in range(1,n+1):
        empty[i]=i**3
    return empty
num=int(input("enter a number : "))
print(cube_finder(num))        
        