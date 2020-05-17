a = [1, 3, 4, 7, 9, 11, 13]
N = len(a)
for i in range(N):
    for j in range(i+1, N):
        if a[i] + a[j] in a:
            print(f'{a[i]} + {a[j]} = {a[i]+a[j]}')

