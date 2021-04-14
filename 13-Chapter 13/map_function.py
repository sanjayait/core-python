# map(function ,input)
nums=[1,2,3,4,5,6,7]
squares=list(map(lambda a: a**2,nums))
print(squares)

# List comprehension
print([i**2 for i in nums])

# Normal method
squares1=[]
for i in nums:
    squares1.append(i**2)
print(squares1)    

# loop in map function
names=['sanjay','kunno','priyanka']
lenth=map(len,names)
for i in lenth:
    print(i)    