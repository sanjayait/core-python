fruits=['grapes','mango','apple','orange']
fruits1=('grapes','mango','apple','orange')
fruits2={'grapes','mango','apple','orange'}
print(sorted(fruits1))


guitars=[
    {'model':'yamaha','price':8400},
    {'model':'naptune','price':35000},
    {'model':'appolo venus','price':20000},
    {'model':'tylor','price':50000}
]
low_to_high=sorted(guitars,key=lambda d:d['price'])
high_to_low=sorted(guitars,key=lambda d1:d1['price'],reverse=True)

print(low_to_high)
print(high_to_low)