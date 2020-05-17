lst1 = [1, 2, 3, 2, 4, 5, 7]
lst2 = [1, 3, 4, 7, 9, 10]

lst1_2 = [x for x in lst1 if x not in lst2]
print(lst1_2)

lst12 = [x for x in lst1 if x in lst2]
print(lst12)


