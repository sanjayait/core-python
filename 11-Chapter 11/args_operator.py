# To make flexible function
def all_total(*args):
    total=0
    for i in args:
        total +=i
    return total
print(all_total(1,2,3,4,5,5,6,7,8))        