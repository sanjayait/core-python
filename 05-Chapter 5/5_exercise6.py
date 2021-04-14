num=[1,3,[4,6,9],7,9,[2,10,21],52,19,[31,48]]
def list_counter(l):
    j=0
    for i in l:
        if type(i)==list:
            j +=1
    return j        
print(list_counter(num))