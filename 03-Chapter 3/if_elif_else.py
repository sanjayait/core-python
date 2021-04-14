age=int(input("enter your age : "))
if age==0 or age <0:
    print("Incorrect age")
elif 0<age<4:
    print("Ticket price : Free")
elif 4<age<13:
    print("Ticket price : 150rs")
elif 13<age<50:
    print("Ticket price : 250rs") 
else:
    print("Ticket price : 200rs")               