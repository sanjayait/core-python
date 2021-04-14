from csv import DictWriter
with open('file2.csv','w',newline="") as f:
    wf=DictWriter(f,fieldnames=['first_name','last_name','age'])
    wf.writeheader()
    # writerow method
    wf.writerow({'first_name':'Sanjay','last_name':'Goyal','age':29})
    wf.writerow({'first_name':'kunno','last_name':'Goyal','age':20})

    # writerows method
    wf.writerows([{'first_name':'Harshal','last_name':'Goyal','age':18}])