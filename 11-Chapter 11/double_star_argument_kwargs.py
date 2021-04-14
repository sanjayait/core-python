# kwargs (Key word argument)
# used in operating dictionaries
def example(**kwargs):
    for j,k in kwargs.items():
       print(f"{j} : {k}")
d=dict(name='sanjay',last_name='goyal')        
example(**d)       # Unpack dictionary by **