# Generate list with range function
# numbers= list(range(1,11))
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# something more about pop method
# print(numbers.pop())

# Index method
# print(numbers.index(5, 5))

# Pass list to a function
def negative_list(l):
    o=l[::-1]
    empty_list=[]
    for i in o:
        empty_list.append(-i)
    return empty_list

      
         
print(negative_list(numbers))