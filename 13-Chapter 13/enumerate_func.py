# We use enumerates fuction with for loop to track possition of our
# Items in iterable

# How we can do this without enumerate function
names=['sanjay','kunno','harshal']
# total=0
# for i in names:
#     print(f"{total} : {i}")
#     total +=1

# With enumerate function
for total,i in enumerate(names):
    print(f"{total} : {i}")

    