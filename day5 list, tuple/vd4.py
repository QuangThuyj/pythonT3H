lst1 = [1, 2, 3, 2, 4, 5, 7]
lst2 = [1, 3, 5, 7, 9, 10]

result = []

for x in lst1:
    if x not in lst2 and x not in result:
        result.append(x)
print(result)