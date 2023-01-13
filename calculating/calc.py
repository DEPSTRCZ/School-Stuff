import math
def calc(a,b):
    x = a//b
    if a/b >= x+0.5:
        return x+1
    else:
        return x

print(calc(5,2))