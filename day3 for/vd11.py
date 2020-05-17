bang_gia = [6, 7, 9, 16]
bang_so = [0, 10, 20, 35]
sonuoc = int(input('So nuoc:'))
sotien = 0
i = 0
N = len(bang_gia)
while sonuoc > 0:
    if i < N-1:
        xmax = bang_so[i+1] - bang_so[i]
        x = min(sonuoc, xmax) #so nuoc o muc gia i
    else:
        x = sonuoc
    sotien += x*bang_gia[i]
    print(f'{x} so nuoc o muc gia {bang_gia[i]}K : {x*bang_gia[i]} K')
    sonuoc -=x
    i += 1

print('Tong tien:', sotien, 'K')
