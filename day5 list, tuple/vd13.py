sale_item = [
    ('P1', 10000, 5),
    ('P2', 20000, 3),
    ('P3', 150000, 3),
    ('P1', 10000, 4),
    ('P3', 150000, 2),
]

counts = []

for item in sale_item:
    name, price, qty = item
    amout = qty*price
    found = False
    for i in range(len(counts)):
        if counts[i][0] == name:
            found = True
            break
    if found:                       #update
        counts[i][1] += qty
        counts[i][2] += amout
    else:                           #add new
        counts.append([name, qty, amout])
counts = sorted(counts, reverse=True, key=lambda x: x[1])
print(counts[0][0])

