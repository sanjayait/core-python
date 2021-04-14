with open('salary.txt','r') as rf:
    with open('salary_output','a') as wf:
        for i in rf.readlines():
            name,salary=i.split(",")
            wf.write(f"{name}\'s salary is rs {salary}")
            