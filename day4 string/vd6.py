tenbien = 'so_ngay_di_lam_trong_thang'

words = tenbien.split('_')
result = ''
for i in words:
    result += i[0].upper() + i[1:].lower()
result = result[0].lower() + result[1:]
print(result)

print()
result = ''
tenbien = 'soNgayDiLamTrongThang'
N = len(tenbien)
for i in range(N):
    c = tenbien[i]
    if c.isupper():
        result += '_'
        
    result += c.lower()

print(result)
