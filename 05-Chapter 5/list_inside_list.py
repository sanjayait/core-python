# List inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]] # 2d list
# 3 item---> 3 lists
print(matrix[2])
for sublist in matrix:
    for i in sublist:
        print(i, end=(','))

# print(type(matrix))   # type function show object class