# Just same as list comprehension
# in this comprehension we use () perenthesis in place of square bracket

square1=[i**2 for i in range(1,11)]  # List comprehension
print(square1)

square2=(i**2 for i in range(1,11))  # Generator comprehension
# for j in square2:
#     print(j)

print(next(square2))
print(next(square2))
print(next(square2))
print(next(square2))