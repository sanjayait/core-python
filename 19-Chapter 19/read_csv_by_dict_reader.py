from csv import DictReader
with open('user_data.csv','r') as f:
    csv_file2 = DictReader(f)
    for row in csv_file2:
        print(row['name'][0])