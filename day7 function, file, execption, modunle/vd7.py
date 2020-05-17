lst = [
    'Hà Nội',
    'Hà Nam',
    'Hà Giang',
    'Hà Tiên'
]

N = len(lst[0])
for st in lst:
    N = min(N, len(lst))
s1 = lst[0]
for i in range(N):
    all_equal = True
    for s in lst:
        if s[i] != s1[i]:
            all_equal = False
            break
    if not all_equal:
        print(i)
        break