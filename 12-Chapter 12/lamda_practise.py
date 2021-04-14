# lamda expression practise
def is_even(a):
    return a%2==0
print(is_even(6))    

is_even2=lambda a: a%2==0
print(is_even2(7))

last_char=lambda s: s[-1]
print(last_char('sanjay'))

# lamda with if_else
func=lambda s: True if len(s)>5 else False
print(func('abcdef'))