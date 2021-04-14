# Generators are iterators
# It gives only one parameter at a time
# you can execute loop in generators
# It consume less space in memory and execute faster


l=[1,2,3,4,5]
i=iter(l)
next(i)
print(next(i))
# memory -----[----------------] lists
# memory ------(2) Generators