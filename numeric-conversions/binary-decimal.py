num = input("Enter the number in decimal:\n")
arr = [int(x)for x in num]
counted = 0
length = len(arr)
for x in arr:
    length -= 1
    counted += (2**length*x)
print(counted)