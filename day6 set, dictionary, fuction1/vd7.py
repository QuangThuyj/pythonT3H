data = [
    {'age': 7, 'height': 120},
    {'age': 15, 'height': 150},
    {'age': 12, 'height': 130},
    {'age': 22, 'height': 165},
    {'age': 25, 'height': 175},
    {'age': 32, 'height': 167},
    {'age': 45, 'height': 180},
]
table = {}

for item in data:
    age, height = item['age'], item['height']
    key = age // 10
    if key not in table:
        table[key] = [item]
    else:
        table[key].append(item)
for k, v in table.items():
    s = sum([x['height'] for x in v])
    print(f'{k*10}-{k*10 + 10}', '->', s/len(v))
print(table)