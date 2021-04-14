# define a function take any list containing numbers... Input---> [1,2,3]
# output----> average of list numbers

average=(lambda a:sum(a)/len(a))
print(average([5,9,4]))

def average_finder(*args):
    average1=[]
    for i in zip(*args):
        average1.append(sum(i)/len(i))
    return average1
print(average_finder([1,2,3],[4,5,6],[7,8,9]))        


# By lambda expression
average_finder2=lambda *args:[sum(i)/len(i) for i in zip(*args)]
print(average_finder2([1,2,3],[4,5,6],[7,8,9]))