# Dictionary comprehension
square={i:i**2 for i in range(1,11)}
# print(square)
for j,k in square.items():
    print(f"Square of {j} is : {k}")


name="sanjay goyal"
word_count={i:name.count(i) for i in name}
# print(word_count) 
for j,k in word_count.items():
    print(f"{j} : {k}")   