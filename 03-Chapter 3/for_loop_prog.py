num1,num2=(input("enter any two number comma seperated : ")).split(",")
num1=int(num1)
num2=int(num2)
total=0
for i in range(num1,num2 +1):
    total +=i
print(f"sum of your range = {total}")
