# fromkeys() method
#if u want give same VALUE for diffrent KEYS
d=dict.fromkeys(('name','age','address'),'unknown')
print(d)

d1=dict.fromkeys("abc",'unknown')
print(d1)    # if we tool one string then it takes every element of string


# get() method
d3={'name': 'Sanjay', 'age': 28, 'address': 'unknown'}
print(d3.get('age'))

if d3.get('names'):
    print('present')
else:
    print('Not present')    