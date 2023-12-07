def calc(op,num):
    match op[0]:
        case "p":
            return num + op[1]
        case "m":
            return num - op[1]
        case "t":
            return num * op[1]
        case "d":
            return num / op[1]
    

def zero(op=None): return calc(op,0) if op else 0

def one(op=None): return calc(op,1) if op else 1

def two(op=None): return calc(op,2) if op else 2

def three(op=None): return calc(op,3) if op else 3

def four(op=None): return calc(op,4) if op else 4

def five(op=None): return calc(op,5) if op else 5

def six(op=None): return calc(op,6) if op else 6

def seven(op=None): return calc(op,7) if op else 7

def eight(op=None): return calc(op, 8) if op else 8

def nine(op=None): return calc(op,9) if op else 9

def plus(*arg):
    return ("p",arg[0])

def minus(*arg):
    return ("m",arg[0])

def times(*arg):
    return ("t",arg[0])

def divided_by(*arg):
    return ("d",arg[0])


x = five(times(two()))+two(times(three()))
#x1 = five(plus(two(times(two(times(four(times(four())))))))) = 69

print(x)