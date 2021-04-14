exa=['abc','tuv','xyz']
def exchange(l):
    empty=[]
    for i in l:
        empty.append(i[::-1])
    # for i in range(len(l)):
    #     empty.append(l[i][::-1])
    return empty
print(exchange(exa))        
# print(exa[0][::-1])
        

