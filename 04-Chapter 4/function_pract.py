# Function practise 
# 1
# def last_char(a):
#     return a[len(a)-1] 
# print(last_char("sanjay"))  


def odd_even(a):
    if a%2==0:
        return"even number"
    return"odd number"      
num=int(input("enter a number : "))
print(odd_even(num))    