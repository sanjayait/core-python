# Filter function
def is_even(a):
    return a%2==0

nums=[3,4,2,1,5,6,9,8,7,10]
evens=tuple(filter(is_even,nums))
new_evens=list(filter(lambda a: a%2==0,nums))
print(evens) 
print(new_evens)   # You can use loop with filter funtion