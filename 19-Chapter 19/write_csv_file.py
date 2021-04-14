from csv import writer
with open('file1.csv','w',newline="") as f:
    wf=writer(f)
    # writerow method
    wf.writerow(['name','country'])
    wf.writerow(['Sanjay','Dubai'])
    wf.writerow(['Kunno','India'])
    wf.writerow(['Harshal','Bhutan'])

    # writerows method
    wf.writerows([['name','country'],['Sanjay','Dubai'],['Kunno','India'],['Harshal','Bhutan']])
