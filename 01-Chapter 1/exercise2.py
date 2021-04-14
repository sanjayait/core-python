# num1=int(input("numone"))
# num2=int(input("numtwo"))
# num3=int(input("numthree"))
# avg=(num1+num2+num3)
# print(avg/3)
# print(f"{(num1+num2+num3)/3}") # old method

num1,num2,num3=input("enter three number comma seperated: ").split(",")
print(f"{(int(num1)+int(num2)+int(num3))/3}") # new method
