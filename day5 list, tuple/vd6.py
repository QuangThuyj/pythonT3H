lst = [1, 3, 4, 5, 6, 7, 8]

lst2 = [x*x for x in lst]

print(lst2)

lst_chan = [x for x in lst if x % 2 == 0]
print(lst_chan)

lst_le = [x for x in lst if x % 2 != 0]
print(lst_le)