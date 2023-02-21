num = int(input("Enter number(DEC):\n"))
def dectobin(num):
    list = []
    while num > 0:
        n = num%2
        num = num//2
        list.append(n)
    list.reverse()
    result = int("".join(str(x) for x in list))
    return result
print(dectobin(num))

