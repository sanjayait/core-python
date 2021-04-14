from functools import wraps
def only_data_type(data_type):
    def decorate(any_fuc):
        @wraps(any_fuc)
        def wrap6(*args,**kwargs):
            if all([type(i)==data_type for i in args]):
                return any_fuc(*args,**kwargs)
            print("invalid arguments")
        return wrap6
    return decorate

@only_data_type(str)
def string_join(*args):
    empty=""
    for j in args:
        empty += j
    return empty

s=['sanjay',' goyal',' kunno',' harshal']
print(string_join(*s))                        