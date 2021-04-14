def even_finder(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
even_nums=even_finder(30)   
for j in even_nums:
    print(j)          