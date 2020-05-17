lst1 = [1, 2, 3, 2, 4, 5, 7]
lst2 = [1, 3, 5, 7, 9, 10]

lst = list(lst1)
lst.extend(lst2)
#lst = lst1 + lst2

result = []

# for x in lst:
#     if x not in result:
#         result.append(x)
# print(result)
# for x in lst1:
#     if x not in result:
#         result.append(x)
# for x in lst2:
#     if x not in result:
#         result.append(x)
for x in lst:
    if x not in result:
        result.append(x)
print(result)



