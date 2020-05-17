d = int(input('Nhap vao ngay cua ban: '))
m = int(input('nhap vao thang cua ban: '))
y = int(input('nhap vao nam cua ban (2000 <= Y <= 2099): '))
if (200 <= y and y <= 2099 and 0 < m <= 12 and 0 < d <= 31):
    if m == 2:
        if ((y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0)):
            if (d <= 29):
                print('Ngay ton tai')
            else:
                print('Ngay khong ton tai')
        else:
            if (d <= 28):
                print('Ngay ton tai')
            else:
                print('Ngay khong ton tai')
    elif ((m % 2 != 0) or m == 8):
        if (d <= 31):
            print('Ngay ton tai')
        else:
            print('Ngay khong ton tai')
    else:
        if (d <= 30):
            print('Ngay ton tai')
        else:
            print('Ngay khong ton tai')
else:
    print('Ngay khong ton tai')


