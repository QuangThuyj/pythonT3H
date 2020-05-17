hoten = input('Nhap vao ho ten day du: ')
arr = hoten.split()
print(arr)

ho = arr[0]
N = len(arr)
ten = arr[N-1]
#if N == 2:
#    tendem =''
#elif N == 3:
#    tendem = arr[1]
#elif N >= 4:
#    tendem = ''
#    for i in range(1, N-1):
#        tendem += arr[i] + ' '


tendem = ' '.join(arr[1:N-1])

print('Ho: ', ho)
print('Tem dem: ', tendem)
print('ten: ', ten)
    
