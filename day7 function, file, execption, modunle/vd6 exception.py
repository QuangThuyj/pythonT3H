import math
import traceback

try:
    a = int(input('a='))
    print('a ** 0.5', math.sqrt(a))
except:
    traceback.print_exc()
finally:
    print('Complete part A')


try:
    b = int(input('b='))
    print('b ** 0.5', math.sqrt(b))
except:
    traceback.print_exc()
