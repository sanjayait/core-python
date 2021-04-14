import pdb

pdb.set_trace()
name=input('enter your name : ')
age=input('enter your age : ')
age2=age + 5                        # Here age is in form of string can't concetenate with int
print(f"current age {name} after 5 years {age2}")