s = input('Nhap vao biet thuc: ')

n = len(s)
if n > 2:
    s1 = 0 #chứa dấu mở ngoặc

    for i in range(len(s)-1):
        if s[i] == '(':
            s1 += 1
        if s[i] == ')':
            if s1 != 0:
                s1 -= 1
            else:
                print("Khong dung")
    if s1 == 0:
        print('dung')

    
        






























































    
    
