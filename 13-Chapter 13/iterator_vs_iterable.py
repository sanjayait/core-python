numbers=[1,2,3,4]  # tuple,strings,list---->iterables
squares=map(lambda a:a**2,numbers)   # iterator

# How loop works
number_iter=iter(numbers)    # loop first convert iterables into iterators
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter))

print(next(squares))        # Here squares already give iterators
print(next(squares))        # so we directy use next func on it 
print(next(squares))