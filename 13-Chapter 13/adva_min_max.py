names=['sanjay','kunno','priyanka','harshal']
def larger(a):
    return len(a)
lenght=min(names, key=larger)
lenght2=max(names, key=lambda a:len(a))    # By lambda function
print(lenght2)                              # You can directly max/min() to print



students=[
    {'name':'sanjay','score':70,'age':29},
    {'name':'kunno','score':80,'age':18},
    {'name':'priyanka','score':90,'age':21}
]
highest=max(students,key=lambda b:b.get('age'))['name']
print(highest)

students2={
    'sanjay':{'score':70,'age':29},
    'kunno':{'score':80,'age':18},
    'priyanka':{'score':90,'age':21}
} 
lowest=min(students2,key=lambda b:students2[b]['age'])
print(lowest)