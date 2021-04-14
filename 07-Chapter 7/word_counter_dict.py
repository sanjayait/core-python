# word counter # sanjay goyal
def word_counter(s):
    empty={}
    for i in s:
        empty[i]= s.count(i)
    return empty

print(word_counter('sanjay goyal'))