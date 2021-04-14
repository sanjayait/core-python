name,char=input("enter your name and a charactor comma seperated: ").split(",")
print(name)
print(f"lenth of your name {len(name.strip())}")
print(f"there are {name.strip().lower().count(char.strip())} charactor in your name") # str format
print("there are "+str(name.strip().lower().count(char.strip()))+" charactor in your name") # simple formate