lst = [1, 2, 3, 4, 5, 6, 2, 4, 5, 6, 2]
#sap xep tang dan
#lst = sorted(lst)
#print(lst)
#sap xep giam dan
#lst = sorted(lst, reverse=True)
#print(lst)

counts = []
for x in lst:
    found = False
    for i in range(len(counts)):
        if counts[i][0] == x:
            found = True
            break
    if found:
        counts[i][1] += 1
    else:
        counts.append([x, 1])
counts = sorted(counts, reverse=True, key=lambda x:x[1])
print(counts)
