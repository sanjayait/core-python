# update method
user1={
'name':'priyanka',
'age': 23,
'fav_movies': [300,'croods','coco'],
'fav_places': ['paris', 'london']
}

more=dict(state='M.P.', hobbies=['gaming','reading'], name='sanjay')

user1.update(more)
print(user1)

# KEY already present then its update with new one
# See here name value also update