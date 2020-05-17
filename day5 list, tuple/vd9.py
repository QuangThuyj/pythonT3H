lst = [1, 3, 5, 10, 14, 17]

R = 3

result = [[]]

left = lst[0]
for x in lst:
    if x <= left + 2*R:
        result[-1].append(x)
    else:
        left = x
        result.append(left)

print(result)