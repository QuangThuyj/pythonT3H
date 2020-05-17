with open('bangdiem.csv', encoding='utf-8') as f:
    header = f.readline().strip()
    lines = f.readlines()

with open('output.csv', 'w', encoding='utf-8') as f:
    new_header = header + ', Điểm TB'
    f.write(new_header + '\n')
    for line in lines:
        stt,hoten,d1,d2,d3 = line.strip().split(',')
        dtb = (float(d1) + 2*float(d2) + 3*float(d3))/6
        f.write(f'{stt}, {hoten}, {d1}, {d2}, {d3}, {dtb} \n')
