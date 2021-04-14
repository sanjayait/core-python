with open('Drdo.txt','r') as rf:
    with open('empty.txt','w') as wf:
        wf.write(rf.read())