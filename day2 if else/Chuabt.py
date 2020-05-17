d = int(input('Nhap vao ngay: ')
m = int(input('Nhap vao thang: '))
y = int(input('Nhap vao nam: '))

max_d = 30
if (m%2 ==1 and m <=7) or (m%2 ==0 and m >= 8):
    max_d =31
if m == 2:
    max_day =29 if y%4 == 0 else 28
if 1 <= m <= 12 and 1 <=d <= max_day:
    print(f'Ton tai ngay {d}/{m}/{y}')
else:
    print(f'Khong ton tai ngay {d}/{m}/{y}')
    
