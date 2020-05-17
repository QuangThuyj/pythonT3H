with open('test.txt') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    for line in lines:
        line = line.strip()
        if line != '':
            f.write(line + "\n")