# Q- what is dictionary?
# A- unordered collection of data in key : value pair

# how to create dictionary
user = {'name': 'sanjay','age': 24}  # key : value

# Another method :
user_info=dict(name='sanjay', age=24)

# How to access data from dictionary
# Note--> there is no indexing becouse of unordered collection of data.
print(user['name'])

# which type of data can store in dictionary.
#anything
user1={
'name':'priyanka',
'age': 23,
'fav_movies': [300,'croods','coco'],
'fav_places': ['paris', 'london']
}
print(user1['fav_movies'])