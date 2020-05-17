s1 = 'Ha Noi'
s2 = 'Ha Giang'

n1 = len(s1) 
n2 = len(s2)
n = min(n1, n2)

for i in range(n):
    if s1[i] != s2[i]:
        print(f'Vi tri khac nahau dau tien la: {i+1}')
        break




