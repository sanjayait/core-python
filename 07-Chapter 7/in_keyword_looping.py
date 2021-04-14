# In keywords and iterations in dictionary.
user1={
'name':'priyanka',
'age': 23,
'fav_movies': [300,'croods','coco'],
'fav_places': ['paris', 'london']
}

# check if key is exist in dict
if 'name'in user1:
    print('present')
else:
    print('not present')    # for checking KEY:

if 'sanjay' in user1.values():
    print('present')
else:
    print('Not present')      # for checking VALUES


# loop in dict
# for i in user1:
#     print(i)      

# for i in user1.values():
#     print(i)

# Values method
# user_val=user1.values()
# print(user_val)

# # Keys method:
# user_keys=user1.keys()
# print(user_keys)

# # Items method:
# user_item=user1.items()
# print(user_item)

for i,j in user1.items():  # Important method
    print(f"{i} : {j}")