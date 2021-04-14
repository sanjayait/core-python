# Example input : l=['abc','tuv','xyz']
#         output---> ['bac','vut','zyx']

string=['abc','tuv','xyz']
def exchange(l):
    return [i[::-1] for i in l]
print(exchange(string))    

