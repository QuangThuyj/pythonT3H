for i in range(1,1001):
    if i % 5 == 3 and i % 7 ==4 and i % 9 == 5:
        print(i)
        break
print('--------')
for i in range(1,1001):
    if i%5 !=3:
        continue
    if i%7 !=4:
        continue
    if i %9 == 5:
        print(i)
        break

print()
