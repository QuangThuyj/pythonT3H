A = [3, 5, 7, 9, 10, 12, 15]
B = [6, 8, 12]
r = 2

def isActive(x):
    return any(abs(b-x) <= r for b in B)
    # for b in B:
    #     if abs(b - x) <= r:
    #         return True
    # return False

for a in A:
    if not isActive(a):
        print(a)