class A:
    def hello(self):
        return 'From class A'
class B:
    def hello(self):
        return 'From class B'
# class C(A,B): # bcz due to method resolution method
class C(B,A):   # We can change preference order 
    pass
ins_c=C()

print(ins_c.hello())