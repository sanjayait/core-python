from csv import reader

with open('user_data.csv','r') as f:
    csv_file1 = reader(f)
    next(csv_file1)
    for row in csv_file1:
        print(row)
