def is_pelindrome(a):
    if a==a[::-1]:
        return True
    return False    

name=input("enter you name : ")
print(is_pelindrome(name))

# def is_pelindrome(a):
#     return a==a[::-1]
# name=input("enter you name : ")
# print(is_pelindrome(name))    