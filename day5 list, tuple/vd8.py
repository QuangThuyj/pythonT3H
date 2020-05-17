lst1 = [2, 3, 5, 9]
lst2 = [0, 7, 8, 12]

min_dist = float('inf')
x1 = x2 = None

for i1 in lst1:
    for i2 in lst2:
        d = abs(i1-i2)
        if d < min_dist:
            min_dist = d
            x1 = i1
            x2 = i2
print(x1, x2)



