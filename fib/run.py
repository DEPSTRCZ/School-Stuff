number = int(input("Zadej číslo:\n"))
print("---------")
if number < 0:print("Chyba: Číslo je záporné!")
mem1 = 0
mem2 = 1
count = 1
while count < number:
    num = mem1+mem2
    print(num)
    mem1 = mem2
    mem2 = num
    count += 1