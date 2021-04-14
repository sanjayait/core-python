num=[1,2,3,4,5,6,7,8]
def reverse_list(l):
    empty=[]
    for i in range(len(l)):
        empty.append((l.pop()))
    return empty
print(reverse_list(num))        