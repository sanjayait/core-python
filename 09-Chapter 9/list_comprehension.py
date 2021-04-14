# With the help of list comprehension we can create of list in one line

# Create a list of square from 1 to 10
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)      # Normal method

# List comprehension method
square2=[i**2 for i in range(1,11)]
print(square2)

names=['Sanjay','Priyanka','Mohit']
firstw=[]
for i in names:
    firstw.append(i[0])
print(firstw)    # Normal method

# list comprehension
first=[i[0] for i in names]
print(first)