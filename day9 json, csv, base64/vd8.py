students = [
    {'name': 'Nguyen Van A', 'diem_hs1': 6, 'diem_hs2': 7, 'diem_hs3': 8},
    {'name': 'Nguyen Van B', 'diem_hs1': 7, 'diem_hs2': 6, 'diem_hs3': 8},
    {'name': 'Nguyen Van C', 'diem_hs1': 6, 'diem_hs2': 6, 'diem_hs3': 7},
    {'name': 'Nguyen Van D', 'diem_hs1': 6, 'diem_hs2': 7, 'diem_hs3': 7}
]

header = ['STT', 'Ten', 'Diem HS1', 'Diem HS2', 'Diem HS3', 'Diem TB']
import csv
with open('student.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    rows = []
    for i, st in enumerate(students):
        name, diem_hs1, diem_hs2, diem_hs3 = st['name'], st['diem_hs1'], st['diem_hs2'], st['diem_hs3']
        diem_tb = (diem_hs1 + diem_hs2*2 + diem_hs3*3)/6
        rows.append([i+1, name, diem_hs1, diem_hs2, diem_hs3, diem_tb])
    writer.writerows(rows)


