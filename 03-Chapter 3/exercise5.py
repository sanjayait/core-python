name,age=input("enter your name and age comma seperated : ").split(",")
age=int(age)
if (name[0]=="a" or name[0]=="A") and age >10:
    print("you can watch coco movie")
else:
    print("sorry,you cannot watch coco movie")
    
