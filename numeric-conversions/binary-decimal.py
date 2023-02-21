num = int(input("Enter the number(BIN):\n"))
def bintodec(num):
    arr = [int(x)for x in str(num)]
    counted = 0
    length = len(arr)
    for x in arr:
        length -= 1
        counted += (2**length*x)
    return counted

print(bintodec(num))