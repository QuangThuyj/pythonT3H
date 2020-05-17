import csv

with open('products.csv', encoding='utf-8') as f:
    f.readline() #Header row
    reader = csv.reader(f, delimiter=';') #Tham so tach
    rows = list(reader)
    for row in rows:
        print(row)