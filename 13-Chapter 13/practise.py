# Practise-->1
# for row in range(1,6):
#     for column in range(1,row+1):
#         print(column, end=(" "))
#     print("")    

# # Practise--->2
# for i in range(6,0,-1):
#     for j in range(i-1,0,-1):
#         print(j,end=(" "))
#     print('')    


# Practise---->3  reverse list
# l=[50,40,30,20,10]
# l1=l[::-1]
# print(l1)    

# Practise--->4 find prime number
# def prime(l):
#     empty=[]
#     for i in l:
#         if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
#             empty.append(i)
#     return empty
# l1=list(range(25,50))
# print(prime(l1))              

# Practise---> 5 factorial
# def factorial(a):
#     total=1
#     for i in range(1,a+1):
#         total *=i
#     return total
# print(factorial(6))      


# Practise--->6
for i in range(1,6):
    for j in range(1,i+1):
        print('@',end=(" "))
    print("")
for k in range(5,1,-1):
    for l in range(k-1,0,-1):
        print('@',end=(" ")) 
    print("")       




