# f = open('test.txt', 'w', encoding='utf-8') #Tham so w la write # encoding = 'utf-8' ghi va doc file TV
# f.write('Xin Chào\n')                       #ghi file
# f.write('Hôm nay là thứ 3 \n')
# f.write('Ngày mai là thứ 4 \n')
# f.close()               # close file

# ghi file
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Xin Chào\n')  # ghi file
    f.write('Hôm nay là thứ 3 \n')
    f.write('Ngày mai là thứ 4 \n')
#Doc toan bo:
with open('test.txt', encoding='utf-8') as f:
    content = f.read()
    print(content)
#doc nhieu dong
with open('test.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
#doc tung dong
with open('test.txt', encoding='utf-8') as f:
    line1 = f.readline()
    print(line1.strip())
    line2 = f.readline()
    print(line2.strip())
#cach 3
with open('test.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# f = open('test.txt', encoding='utf-8')    #tham so r la read mac dinh k can truyen vao
# content = f.read()      #doc file
# f.close()
# print(content)



