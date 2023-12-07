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
    

def zero(op=None):
    if op:
        return calc(op,1)
    else:
        return 1

def one(op=None):
    if op:
        return calc(op,1)
    else:
        return 1

def two(op=None):
    if op:
        return calc(op,2)
    else:
        return 2

def three(op=None):
    if op:
        return calc(op,3)
    else:
        return 3

def four(op=None):
    if op:
        return calc(op,4)
    else:
        return 4

def five(op=None):
    if op:
        return calc(op,5)
    else:
        return 5

def six(op=None):
    if op:
        return calc(op,6)
    else:
        return 6

def seven(op=None):
    if op:
        return calc(op,7)
    else:
        return 7

def eight(op=None):
    if op:
        return calc(op,8)
    else:
        return 8

def nine(op=None):
    if op:
        return calc(op,9)
    else:
        return 9

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