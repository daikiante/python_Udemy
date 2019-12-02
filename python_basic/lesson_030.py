import csv

with open('/Users/daikiyamada/Desktop/ex.csv', 'w') as csv_file:
    fildnames = ['Name','Count']
    writer = csv.DictWriter(csv_file, fieldnames=fildnames)
    writer.writeheader()
    writer.writerow({'Name': '名前','Count': '年齢'})


answer = input('まだ入力しますか? (y/n):')
while answer == y:
    name = input('名前はなんですか? :')
    age = input('年齢はいくつですか? :')
    with open('/Users/daikiyamada/Desktop/ex.csv', 'a') as csv_file:
    fildnames = ['Name','Count']
    writer = csv.DictWriter(csv_file, fieldnames=fildnames)
    writer.writeheader()
    writer.writerow({'Name': name,'Count': 1})



