odd_even={i : ('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(odd_even)
for j,k in odd_even.items():
    print(f"{j} : {k}")