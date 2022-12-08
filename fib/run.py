number = int(input("Zadej číslo:\n"))
print(0)
print(1)
print(1)
mem1 = 1
mem2 = 0
count = 1
while count < number:
    x = count+mem1
    print(x)
    mem1 = x
    count += 1