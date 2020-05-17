Nmax = 50
with open('text.txt', encoding='utf-8') as f:
    lines = f.readlines()

with open('output-btvn.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        line = line.strip()
        while len(line) > Nmax:
            pos = line[:Nmax].rfind(' ')
            if pos < 0: pos = Nmax
            f.write(line[:pos] + '\n')
            line = line[pos:]
        f.write(line + '\n')
