st = input('Nhap vao ten nguoi/TP:')
arr = st.split()

result = ''

for word in arr:
    result += word[0].upper() + word[1:].lower() + ' '
print(result)
