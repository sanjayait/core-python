# Zip function
user_id=['user1','user2','user3']
names=['sanjay','kunno','priyanka']
combine=(zip(user_id,names))
# print(list(combine))  # you can change into dictionary also
print(dict(combine))

# You can zip more than 2 varible
last_names=['goyal','sharma','tiwari']
all=zip(user_id,names,last_names)
print(list(all))

# zip() used for unpacking with *args argument
l=[(1,2),(3,4),(5,6),(7,8)]
l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))
