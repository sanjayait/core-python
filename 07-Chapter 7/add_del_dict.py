# Add and Delete data in dict
user1={
'name':'priyanka',
'age': 23,
'fav_movies': [300,'croods','coco'],
'fav_places': ['paris', 'london']
}

# How to add data 
user1['fav_songs']=['song1','song2']
print(user1)

# Pop() method
# user1.pop('age')  # For pop selected KEY , Atleast one argument pass krana pdega
# print(user1)

# pop() item method  # For popitem for random KEY
user1.popitem()
print(user1)


