def calcAreaAndPerimeter(w, h):
    S = w*h
    P = 2*(w+h)
    return S, P

S, P = calcAreaAndPerimeter(5, 4)

print(S, P)

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

print(add(2, 3))
print(sub(5, 4))