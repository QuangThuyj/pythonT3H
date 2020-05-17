a = [1,2,3,4,5,6,7,8,9,12,15]
s = 0
for x in a:
    s += x
print(f'Tong cua day a la: {s}')
print()

a = [1,3,5,7,9,10,12]
N = len(a)
found = False
for i in range(N):
    if a[i]%2 == 0:
        print(a[i])
        found = True
        break
if not found:
    print('Khong co so chan')
