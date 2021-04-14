# set is data type
# unordered collection of uniqe items

s={1,2,3,2}
print(s)
l=[1,2,3,3,4,4,5,6,6,7,7,7,8]
s2=set(l)
l2=list(set(l))
# print(s2)
print(l2)

# to add items to set
s.add(4)
s.add(5)
print(s)

# to remove items to set
s.discard(5)
print(s)