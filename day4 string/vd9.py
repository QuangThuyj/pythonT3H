st = 'Hom nay la ngay 29/12/2019, ....'
N = len(st)
found = False
for i in range(N):
    if st[i].isdigit():
        print(i)
        found = True
        break
if not found: print('No digit found')
print()

password = input('password: ')
length_gte8 = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
#for c in password:
#    if c.isupper():
#        has_upper = True
#        break

#has_digit = False
#for c in password:
#    if c.isdigit():
#        has_digit = True
#        break
if not length_gte8:
    print('password > 8')
if not has_upper:
    print('password co it nhat 1 chu viet hoa')
if not has_digit:
    print('password co it nhat 1 chu so')
if length_gte8 and has_upper and has_digit:
    print('password hop le')
    
