from csv import DictReader,DictWriter
with open('file2.csv','r') as f:
    with open('file3.csv','w',newline="") as w:
        rf=DictReader(f)
        wf=DictWriter(w,fieldnames=['first_name','last_name','age'])
        wf.writeheader()
        for i in rf:
            fname,lname,ag=i['first_name'],i['last_name'],i['age']
            wf.writerow({'first_name':fname,'last_name':lname,'age':ag})