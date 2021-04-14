nums=list(range(1,11))
def arrange(l):
    return [i*2 if i%2==0 else -i for i in l]   # List comprehension method

    # empty=[]
    # for i in l:
    #     if i%2==0:
    #         empty.append(i*2)
    #     else:
    #         empty.append(-i)
    # return empty        
print(arrange(nums))             # Normal method


# Nested list comprehension
num_list=[[i for i in range(1,5)] for j in range(3)]
print(num_list)
