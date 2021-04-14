mixed=(1,2,3,4.6)

# looping in tuples
for i in mixed:
    print(i)
# Note you can use while loop also

# tuple with one element
num=(1,)  # if we create one element then ',' must be needed
word=('papita',)  # if ',' does not present then its only string not a tuple

# tuple without parenthesis
guitars= 'yamaha','baton rouge','taylor' # it is treated as tuple

# List inside tuple
cars=('ford','maruti',['honda','hyndai'],'BMW') # you can modify list inside tuple
cars[2].append('tata')
print(cars)

# tuple unpacking
fruits=('mango','orange','apple')
fruit1,fruit2,fruit3=(fruits)
print(fruit3)

# function we can used with tuple
# min(), max(), sum()