num=[1,2,3,4,5,6,7,8,9]
def filter_odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    # output=[odd, even]   # alag variable bhi bna skte hai
    return [odd,even]      # direct return bhi kr skte hai
print(filter_odd_even(num))               