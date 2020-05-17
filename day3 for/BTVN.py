M = float(input('Nhap vao so tien phai tra: '))
M0 = float(input('Nhap vao so tien da tra: '))
m = float(input('Nhap vao so tien tra gop hang thang: '))
r = float(input('Nhap vao lai suat tra gop (%/nam): '))
r1 = r/12/100
M1 = M - M0 #so tien con lai phai tra gop

n = 1 #so thang tra gop
while (M1*(1+r1)**n - (m/r1)*((1+r1)**n - 1)) > 0:
    n += 1
print(n)


