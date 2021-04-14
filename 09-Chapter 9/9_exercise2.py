# Define a function num to string
# Input--> [True,False,[1,2,3],4.3,5.7,'aba',8,6]
# Output--> [1,2,3,4,5,6,7,8]

lists=[True,False,[1,2,3],4.3,5.7,'aba',8,6]
def select_num(l):
    return[str(i) for i in l if (type(i)==int or type(i)==float)]
print(select_num(lists))    