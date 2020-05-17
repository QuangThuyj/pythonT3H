st = input('Nhap vao biet thuc: ')
mo = dong = 0
valid = True

for c in st:
    if c == '(':
        mo += 1
    if c == ')':
        dong += 1
    if dong > mo:
        valid = False
        break
valid = valid and (dong == mo)
print(valid)
 
