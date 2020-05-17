m = int(input('So tien gui ban dau: '))
r = int(input('Lai suat (%/nam):'))
t = int(input('Ky han (thang): '))
laisuat = r*t/12
for i in range(5):
    tienLai = m*laisuat/100
    m += tienLai
print(round(m))


