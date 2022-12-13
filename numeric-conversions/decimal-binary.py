cislo = int(input("Enter number:\n"))
x = cislo
list = []
while x > 0:
    n = x%2
    x = x//2
    list.append(n)
list.reverse()
print(list)


