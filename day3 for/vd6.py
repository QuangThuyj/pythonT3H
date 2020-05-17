a = [5, 7, 3, 9, 10, 30, 50, 60, 30, 10, 5]

s = sum(a)
N = len(a)
s1 = 0
for i in range(N):
    s1 += a[i]
    if s1 >= s/2:
        print(f'trung vi la vi tri thu: {i}')
        break
    
