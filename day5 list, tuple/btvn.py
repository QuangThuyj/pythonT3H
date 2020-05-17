para = str(input('Nhap vao doan van ban'))

lst = para.split()
print(lst)

counts = []
for word in lst:
    found = False
    for i in range(len(counts)):
        if counts[i][0] == word:
            found = True
            break
    if found:
        counts[i][1] += 1
    else:
        counts.append([word, 1])
counts = sorted(counts, reverse=True, key=lambda x:x[1])
print(counts)