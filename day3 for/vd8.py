x = 1
while not(x%5 == 3 and x%7 == 4):
     x += 1
print(x)


K = int(input('K = '))
S = 0
i = 1

while S < K:
    S += i
    i += 1

print(i-1)
