lst = [1, 2, 1, 3, 4, 1, 2, 5, 3]

count = {}
for x in lst:
    count[x] = count.get(x,0) + 1
    # if x not in lst:
    #     count[x] = 1
    # else: 
    #     count[x] += 1

print(count.items())