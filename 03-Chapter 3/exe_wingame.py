num=input("choose any number b/t 01-20 : ")
num=int(num)
win=int(11)

if num==win:
    print("YOU WIN !!") 
else:                             #nested if_else
    if num <win:
        print("low from winning number")
    else:
        print("high from winning number")           