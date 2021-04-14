# any(), all() functions
num1=[2,4,6,8]
num2=[1,2,5,7]

print(all([i%2==0 for i in num1]))

print(any([i%2==0 for i in num2]))