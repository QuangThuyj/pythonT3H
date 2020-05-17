danso = 95.5
nam = 2017
tocdo_tang = 1.1

while danso < 120:
    luong_tang = danso*tocdo_tang/100
    danso += luong_tang
    nam += 1
print(nam, danso)

print()

M =int(input('Tien gui ban dau: '))
M2 = int(input('So tien muon dat toi: '))
r = float(input('Lai suat tien gui (%/nam): '))
T = int(input('Ky han gui (thang): '))
i = 0
while M < M2:
    tienLai = M*(r*T/12)/100
    M += tienLai
    i += 1
print(i, M)


