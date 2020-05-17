lst = [1, 3, 4, 5, 6, 7, 8, 10, 12]

lst_chan = []
lst_le=[]

for i in lst:
    if i % 2 == 0:
        lst_chan.append(i)
    if i % 2 != 0:
        lst_le.append(i)

print('so chan', lst_chan)
print('so le', lst_le)