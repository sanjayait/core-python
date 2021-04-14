nums=list(range(1,11))
even_num=[]
for i in nums:
    if i%2==0:
        even_num.append(i)
print(even_num)        


# List comprehension method
even_num2=[i for i in nums if i%2==0]
print(even_num2)
odd_num=[i for i in range(1,11) if i%2 !=0]
print(odd_num)