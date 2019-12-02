# csvファイルの書き込み

import csv

with open('test.csv', 'w') as csv_file:
    fildnames = ['Name','Count']
    writer = csv.DictWriter(csv_file, fieldnames=fildnames)
    writer.writeheader()
    writer.writerow({'Name': 'A','Count': 1})
    writer.writerow({'Name': 'B','Count': 2})



# csvファイルの読み込み

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
        