
while True:
    x = int(input('x = '))
    y = int(input('y = '))
    z = x + y
    print(f'{x} + {y} = {z}')
    anw = input('Tiep tuc (Y/N): ')
    if anw.upper() != 'Y':
        break
