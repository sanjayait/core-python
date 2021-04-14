num=input("enter any numer one or more then two digits :  ")
#12345
total=0
for i in range(len(num)):
    total +=int(num[i])
print(f"sum of your number - {total}")