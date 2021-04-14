# Create generator function
def nums(n):
    for i in range(1,n+1):
        yield i

for j in nums(10):
    print(j)        